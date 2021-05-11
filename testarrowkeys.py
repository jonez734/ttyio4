import ttyio4 as ttyio

done = False
while not done:
    ch = ttyio.getch(noneok=False)
#    ttyio.echo("ch=%r" % (ch))
    if ch == "":
        continue
    if ch == "\n":
        break
    ttyio.echo("%r" % (ch))
