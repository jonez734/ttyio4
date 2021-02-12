import ttyio4 as ttyio

for x in range(0, 50):
    ttyio.echo("x=%r" % (x))
    ch = ttyio.getch(noneok=True)
    if ch == "/":
        ttyio.echo("slash detected")
        break
    elif ch == " ":
        ttyio.inputchar("*paused*", " ", "")
        ttyio.echo("{CHA}{EL}", end="")
