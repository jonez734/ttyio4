# ttyio4

## links

- [writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer) served as inspiration for the current generation lexer to handle mci commands.
- [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)
- 'readlike': python3-readlike-0.1.3-1.fc33.noarch.rpm 
- http://www.cse.psu.edu/~kxc104/class/cse472/09f/hw/hw7/vt100ansi.htm
- https://emu.edu/marketing/docs/emu-brand-identity.pdf
- https://www.google.com/search?sxsrf=ALeKk01V-5vWfsbzppvZIHeziwKjMjOT1g:1628047373683&q=emich+color+gray&tbm=isch&chips=q:emich+color+gray,online_chips:heather+grey:uOX_WuOoSUo%3D&usg=AI4_-kQZSiTC0UndLOXXUhAtctE7eRJEWA&sa=X&ved=2ahUKEwjiy4qLtZbyAhUmAZ0JHYxZCR8QgIoDKAN6BAgIEBo&biw=1920&bih=982
- https://encycolorpedia.com/9aa297#:~:text=Paints-,Benjamin%20Moore%20Heather%20Gray%20%2F%202139%2D40%20%2F%20%239aa297%20Hex,%25%20saturation%20and%2061%25%20lightness.
- https://docs.python.org/3/library/re.html
- https://docs.python.org/3/howto/regex.html#regex-howto
- https://unix.stackexchange.com/questions/184345/detect-how-much-of-unicode-my-terminal-supports-even-through-screen?noredirect=1&lq=1


## todo

- [ ] gray out menuitems which do not meet requirements, including not allowing the option letter
- [ ] add kw arg to specify how \n is handled (space vs empty vs {f6})
- [ ] pluggable mcicommand tables
- [x] fix {f6:42} (prints a couple of newlines) (was using the wrong regexp group for the multiple)
- [x] pick a bgcolor/color for level="debug" in echo()
- [x] handle arrow keys (\x1b[A, etc).. maybe ftell() will work? no, sys.stdin is not seekable
- [ ] variables
  * recursive
  * setvariable(name, value) - set variable <name> to <value>
  * getvariable(name) - returns variables[name] if name exists, else None (which is also a valid value. only other option would be to raise an exception)
  * clearvariables() - resets the variables dict to empty
  * usage: {var:<name>} in echo()
  * [x] wordwrap does not work right if a var has a command in it ("{green}eggs"), which needs to work for displaymenu() to be customizable.
- [ ] getch
  * gets a single char using select/read for async
  * since ~may 2021, working to add handling of cursor keys, backspace, home, end, ctrl-u.
  * thought about trying ftell() to handle arrow keys, but sys.stdin is not seekable.
  * settled on making a loop that reads one byte at a time, setting a flag when it's an esc, and then returning a string like 'KEY_CURSORDOWN', etc
  * when handling backspace, it will not work to move the cursor left and erase to end-of-line (libreadline should be emulated). 
  * solution is to backspace, print a space, then backspace again. also update the buffer and position
  * [ ] handle hitting esc and returning KEY_ESC while also handling cursor keys and home/end/etc?
  * home, ctrl-a
  * end, ctrl-e
  * [ ] on EOF, raise EOFError
- [x] slow performance of echo()
- [x] getch() does not do well when using a key (like F5) that has not been placed into a table. ctrl-c is required.
- [ ] plus/4 palette: https://en.wikipedia.org/wiki/MOS_Technology_TED needs rgb values.
- [x] change inputboolean() so that "YN" is the default set of options (instead of YNTF)
- [x] ctrl-u stops at pos=1 instead of 0
- [x] add {wait:<seconds>} aka \w<seconds> in imagebbs
- [x] adjust {wait} to use 0.250 seconds instead of 1.00
- [x] add handling for card suits (code page 437). https://en.wikipedia.org/wiki/Code_page_437
- [ ] https://en.wikipedia.org/wiki/File:VTTEST-doublesize.png
- [ ] move collapselist() to bbsengine5
- [ ] handle unicode strings (emojis, box characters, card suits)
 * '\U0001xxxx' is the key (cap U, prefix with three 0s)
 * https://stackoverflow.com/questions/3220031/how-to-filter-or-replace-unicode-characters-that-would-take-more-than-3-bytes
 * https://en.wikipedia.org/wiki/Emoticons_(Unicode_block)
 * https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e
 * https://unicode.org/emoji/charts/emoji-list.html
 * https://medium.com/analytics-vidhya/how-to-print-emojis-using-python-2e4f93443f7e
 * https://stackoverflow.com/questions/10569438/how-to-print-unicode-character-in-python
- [ ] if no pattern matches in echo(), 'mismatch' takes over and displays the command and all following commands as plain text
- [ ] in getch(), poll for notifications
- [ ] handle signal.SIGHUP same as EOF and INTR
- [x] handle {var} using yield: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
- [ ] check for recursion in {var} commands
  * [problem of recursive includes](https://andybargh.com/problem-of-recursive-includes/)
- [ ] detect unicode support
  * https://serverfault.com/questions/13898/how-to-find-out-if-a-terminal-supports-utf-8
  * https://unix.stackexchange.com/questions/10698/timing-out-in-a-shell-script
  * https://unix.stackexchange.com/a/250063
- [ ] optimize-- store previous command, do not emit twice
- [x] optimization
  * move color and bgcolor to their own tables,
  * add handlecommand() subfunction.
  * side-effect is that if a syntax error exists e.g. {syntaxerror}, it will output a message.
  * prolly did help performance all that much.
  * helps w the ability to override the tables

## notes
- order of patterns is critical. do not mess with it, else many code changes will be triggered
- DECDWL/DECDHL (double height, double width) -- not supported by gnome-terminal (vte)
  * https://gitlab.gnome.org/GNOME/vte/-/issues/195
  * https://gitlab.freedesktop.org/terminal-wg/specifications/-/issues/9
  * konsole (kde) does double height, but not double width.
  * perhaps set up an echo/read loop similar to detecting ansi that can figure out if double height is supported.
  * https://en.wikipedia.org/wiki/ANSI_escape_code#Terminal_input_sequences
  * https://stackoverflow.com/questions/3470106/printing-double-size-characters-with-ncurses
- for a specific app, need a way to find out the ascii value of the character under the cursor
  * https://unix.stackexchange.com/questions/76742/is-it-possible-to-get-a-character-at-terminal-cursor-using-ansi-escape-codes
  * mvinch() (ncurses)
  * https://stackoverflow.com/questions/35961761/how-can-i-get-a-character-in-a-position-of-the-screen-with-ncurses-in-c
- https://unix.stackexchange.com/questions/255707/what-are-the-keyboard-shortcuts-for-the-command-line/255735 --- list of editing shortcuts
- figure out max length of the buffer, check to see if buf is that length, and if there has not been a match, reset flag and buffer. ty pscug 20210627
- check for failure. if I am at maxlength of buffer, and the lookup fails, reset buffer and flag.
- watch for escape sequences I care about from a table and ignore the seq that are not interesting.
- code page 437 (ibm character set)
  * https://en.wikipedia.org/wiki/Code_page_437
  * https://www.google.com/search?q=linux+how+do+I+enter+unicode+characters+from+a+different+page&oq=linux+how+do+I+enter+unicode+characters+from+a+different+page&aqs=chrome..69i57.10027j0j7&sourceid=chrome&ie=UTF-8
  * https://www.ascii-codes.com/
  * https://www.google.com/search?q=code+page+437+names&oq=code+page+437+names&aqs=chrome.0.69i59.3385j0j7&sourceid=chrome&ie=UTF-8
