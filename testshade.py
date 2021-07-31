import ttyio4 as ttyio

terminalwidth = ttyio.getterminalwidth()

ttyio.echo("{darkgray}{unicode:lightshade}", end="") # 1
ttyio.echo("{darkgray}{unicode:mediumshade}", end="") # 2
ttyio.echo("{gray}{unicode:lightshade}", end="") # 3
ttyio.echo("{gray}{unicode:mediumshade}", end="") # 4
ttyio.echo("{gray}{unicode:darkshade}", end="") # 5
ttyio.echo("{lightgray}{unicode:mediumshade}", end="") # 6
ttyio.echo("{white}{unicode:solidblock}", end="") # 7
ttyio.echo("{bgwhite}{black}%s{/all}" % ("happy birthday 2021, mom!".center(terminalwidth-14)), end="")
ttyio.echo("{white}{unicode:solidblock}", end="") # 7
ttyio.echo("{lightgray}{unicode:mediumshade}", end="") # 6
ttyio.echo("{gray}{unicode:darkshade}", end="") # 5
ttyio.echo("{gray}{unicode:mediumshade}", end="") # 4
ttyio.echo("{gray}{unicode:lightshade}", end="") # 3
ttyio.echo("{darkgray}{unicode:mediumshade}", end="") # 2
ttyio.echo("{darkgray}{unicode:lightshade}", end="") # 1
ttyio.echo("{/all}")
