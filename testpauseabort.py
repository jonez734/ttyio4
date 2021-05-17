import ttyio4 as ttyio

def test_pauseabort():
    for x in range(0, 50):
        ttyio.echo("x=%r" % (x))
        ch = ttyio.getch(noneok=True, echoch=False)
        if ch == "/" or ch == "Q":
            ttyio.echo("*aborted*")
            break
        elif ch == " ":
            ch = ttyio.inputchar("*paused*", "Q/ ", "", echoch=False)
            ttyio.echo("{CHA}{EL}", end="")
            if ch == "Q" or ch == "/":
                ttyio.echo("*aborted*")
                break

def testinputchar():
    ch = ttyio.inputchar("prompt: ", "ABCDE", noneok=True)
    ttyio.echo("ch=%r" % (ch))
    
try:
    test_pauseabort()
    # testinputchar()
except KeyboardInterrupt:
    ttyio.echo("INTR")
except EOFError:
    ttyio.echo("EOF")
