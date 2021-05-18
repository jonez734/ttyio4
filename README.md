# ttyio4

## links

- [writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer) served as inspiration for the current generation lexer to handle mci commands.
- [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)
- 'readlike': python3-readlike-0.1.3-1.fc33.noarch.rpm 

## todo

- [ ] add kw arg to specify how \n is handled (space vs empty vs {f6})
- [ ] pluggable mcicommand tables
- [x] fix {f6:42} (prints a couple of newlines) (was using the wrong regexp group for the multiple)
- [x] pick a bgcolor/color for level="debug" in echo()
- handle arrow keys (\x1b[A, etc).. maybe ftell() will work? no, sys.stdin is not seekable
- [ ] variables
  * not recursive
  * setvariable(name, value) - set variable <name> to <value>
  * getvariable(name) - returns variables[name] if name exists, else None (which is also a valid value. only other option would be to raise an exception)
  * clearvariables() - resets the variables dict to empty
  * usage: {var:<name>} in echo()
- [ ] getch
  * gets a single char using select/read for async
  * since ~may 2021, working to add handling of cursor keys, backspace, home, end, ctrl-u.
  * thought about trying ftell() to handle arrow keys, but sys.stdin is not seekable.
  * settled on making a loop that reads one byte at a time, setting a flag when it's an esc, and then returning a string like 'KEY_CURSORDOWN', etc
  * when handling backspace, it will not work to move the cursor left and erase to end-of-line (libreadline should be emulated). 
  * solution is to backspace, print a space, then backspace again. also update the buffer.
  * [ ] how to handle hitting esc and returning KEY_ESC while also handling cursor keys and home/end/etc?
  * home, ctrl-a
  * end, ctrl-e
  * [ ] on EOF, raise EOFError
- [ ] performance of echo() (slow)

## notes

- order of patterns is critical. do not mess with it, else many code changes will be triggered
- DECDWL/DECDHL (double height, double width) -- not supported by gnome-terminal (vte)
  * https://gitlab.gnome.org/GNOME/vte/-/issues/195
- for a specific app, need a way to find out the ascii value of the character under the cursor
  * https://unix.stackexchange.com/questions/76742/is-it-possible-to-get-a-character-at-terminal-cursor-using-ansi-escape-codes
  * mvinch() (ncurses)
  * https://stackoverflow.com/questions/35961761/how-can-i-get-a-character-in-a-position-of-the-screen-with-ncurses-in-c
