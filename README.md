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


