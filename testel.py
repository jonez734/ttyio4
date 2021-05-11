import ttyio4 as ttyio

terminalwidth = ttyio.getterminalwidth()
ttyio.echo("{home}{clear}", end="")
ttyio.echo("{curpos:0,0}", end="")
ttyio.echo("foo bar baz bing foo bar baz bing foo bar baz bing ".ljust(terminalwidth-2, "*"), end="")
ttyio.echo("{home}alpha bravo charlie delta{el}{f6}")
