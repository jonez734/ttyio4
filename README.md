# ttyio4

## links

- [writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer) served as inspiration for the current generation lexer to handle mci commands.
- [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

## todo

- [ ] add kw arg to specify how \n is handled (space vs empty vs {f6})
- [ ] pluggable mcicommand tables
- [x] fix {f6:42} (prints a couple of newlines) (was using the wrong regexp group for the multiple)

## notes

- for some reason, the order of the expressions in token_specification are order sensitive (mismatched parens?)
  * if I put ERASELINE below ACS in the list, the offset required for ACS shifts.
  * after reordering of the token spec, I had to fix {f6} because the group offset changed.
  * afaik, all of the regexps are balanced and syntax-error free.
  * sucinct: every pattern is in a group. if I change the order of the groups, it makes sense that the offsets will change.
  * solution: ?
