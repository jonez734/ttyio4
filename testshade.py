import ttyio4 as ttyio

terminalwidth = ttyio.getterminalwidth()

ttyio.echo("{darkgray}{unicode:lightshade}{unicode:mediumshade}", end="")
ttyio.echo("{gray}{unicode:lightshade}{unicode:mediumshade}{unicode:darkshade}", end="")
ttyio.echo("{lightgray}{unicode:mediumshade}", end="")
ttyio.echo("{white}{unicode:mediumshade}", end="")
ttyio.echo("{unicode:solidblock}", end="")
ttyio.echo("{bgwhite}{black}%s{/all}" % ("happy birthday 2021, mom!".center(terminalwidth-16)), end="")
ttyio.echo("{white}{unicode:solidblock}", end="")
ttyio.echo("{unicode:mediumshade}", end="")
ttyio.echo("{lightgray}{unicode:mediumshade}", end="")
ttyio.echo("{gray}{unicode:lightshade}{unicode:mediumshade}{unicode:darkshade}", end="")
ttyio.echo("{darkgray}{unicode:lightshade}{unicode:mediumshade}{/all}", end="")

# Happy Birthday 2021, Mom!{/all}")
