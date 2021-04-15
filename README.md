# ttyio4

## links

- [writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer) served as inspiration for the current generation lexer to handle mci commands.
- [Build your own Command Line with ANSI escape codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

## todo

- [ ] add kw arg to specify how \n is handled (space vs empty vs {f6})

## notes

- for some reason, the order of the expressions in token_specification are
  order sensitive (mismatched parens?)-- if I put ERASELINE below ACS in the
  list, the offset required for ACS shifts.
- afaik, all of the regexps are balanced and syntax-error free.
