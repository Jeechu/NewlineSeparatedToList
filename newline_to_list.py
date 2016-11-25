import sublime
import sublime_plugin

class NewlineToListCommand(sublime_plugin.TextCommand):
  def perform(self, value):
    # Actually perform the task
    self.view.run_command('perform_newline_to_list', {'args': {'type': self.quote_type, 'bracket': value}})

  def run(self, edit, quote_type):
    # Take quote_type as input argument from command
    self.quote_type = quote_type

    # Get settings
    settings = sublime.load_settings('Preferences.sublime-settings')
    show_quick_panel = settings.get('ask_for_bracket_type')
    default_bracket = self.get_bracket_index(settings.get('default_bracket_type'))

    if show_quick_panel or (default_bracket is None):
      # Ask user for bracket type
      bracket_type_list = ["Curved ()", "Square []", "Curly {}", "None"]
      self.view.window().show_quick_panel(bracket_type_list, self.perform)
    else:
      self.view.run_command('perform_newline_to_list', {'args': {'type': self.quote_type, 'bracket': default_bracket}})

  def get_bracket_index(self, bracket_type):
    if bracket_type == 'curved':
      return 0
    elif bracket_type == 'square':
      return 1
    elif bracket_type == 'curly':
      return 2
    elif bracket_type == 'none':
      return 3
    else:
      return None

class PerformNewlineToListCommand(sublime_plugin.TextCommand):
  def run(self, edit, args):
    quote_type = args['type']
    bracket = args['bracket']

    if quote_type == "single" or quote_type == "dynamic_single":
      quote = "\'"
      escaped_quote = "\\\'"
    elif quote_type == "double" or quote_type == "dynamic_double":
      quote = "\""
      escaped_quote = "\\\""
    elif quote_type == "none":
      quote = ""
      escaped_quote = ""
    else:
      return

    open_bracket = "("
    close_bracket = ")"
    if bracket == 0:
      open_bracket = "("
      close_bracket = ")"
    elif bracket == 1:
      open_bracket = "["
      close_bracket = "]"
    elif bracket == 2:
      open_bracket = "{"
      close_bracket = "}"
    elif bracket == 3:
      open_bracket = ""
      close_bracket = ""
    elif bracket == -1:
      return

    # Get selected region(s)
    selections = self.view.sel()
    for region in selections:
      # If nothing is selected, get complete file
      if region.empty():
        region = sublime.Region(0, self.view.size())

      if quote_type.startswith("dynamic"):
        # Split region at newline and create list of each line if content of individual line is not empty, and also add quotes around the content
        all_lines = [self.view.substr(line) if self.view.substr(line).isdigit() else quote+self.view.substr(line).replace(quote, escaped_quote)+quote for line in self.view.split_by_newlines(region) if self.view.substr(line) != ""]
      else:
        # Split region at newline and create list of each line if content of individual line is not empty, and also add quotes around the content
        all_lines = [quote+self.view.substr(line).replace(quote, escaped_quote)+quote for line in self.view.split_by_newlines(region) if self.view.substr(line) != ""]

      # join all lines seperated by command followed by space, wrapped by brackets
      new_content = ", ".join(all_lines)
      if new_content != "":
        new_content = open_bracket + ", ".join(all_lines) + close_bracket
      # Reaplace the region (selected or complete) with new content
      self.view.replace(edit, region, new_content)
      
