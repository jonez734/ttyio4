# ttyio4

## links

- [writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer) served as inspiration for the current generation lexer to handle mci commands.
- [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

## todo

- [ ] add kw arg to specify how \n is handled (space vs empty vs {f6})
- [ ] pluggable mcicommand tables
- [x] fix {f6:42} (prints a couple of newlines) (was using the wrong regexp group for the multiple)
- [x] pick a bgcolor/color for level="debug" in echo()
- handle arrow keys (\x1b[A, etc).. maybe ftell() will work?
- [ ] variables
  * setvariable(name, value) - set variable <name> to <value>
  * getvariable(name) - returns variables[name] if name exists, else None (which is also a valid value. only other option would be to raise an exception)
  * clearvariables() - resets the variables dict to empty
  * usage: {var:<name>} in echo()
- [ ] how to handle hitting esc and returning KEY_ESC?

## notes

- order of patterns is critical. do not mess with it
