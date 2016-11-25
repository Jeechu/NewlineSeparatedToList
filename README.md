# NewlineSeperatedToList for Sublime Text 3

This package makes converting newline seperated document (or selection of document) to a list easier.

## Settings

Set `ask_for_bracket_type` to `false` and `default_bracket_type` to avoid having to select backet type every time.
> NOTE: Setting `ask_for_bracket_type` and not setting `default_bracket_type` will show the prompt to select bracket anyway.

```JSON

  {
    "ask_for_bracket_type": false,
    "default_bracket_type": "curved"
  }
```
#### Accepted bracket types

| Bracket Type | Example |
|--------------|---------|
| curved       | ( )     |
| square       | [ ]     |
| curly        | \{ \}   |
| none         |         |

## Usage

Tools -> Command Palette (Ctrl+Shift+P or Cmd+Shift+P)

Options:
* **Newline to List: Double quotes** - adds double quotes to each item in list, escapes any double quotes already present
* **Newline to List: No quotes** - no quotes will be added
* **Newline to List: Single quotes** - adds single quotes to each item in list, escapes any single quotes already present
* **Newline to List: Dynamic double quotes** - adds double quotes to each non-digits item in list, escapes any double quotes already present
* **Newline to List: Dynamic single quotes** - adds single quotes to each non-digits item in list, escapes any single quotes already present
