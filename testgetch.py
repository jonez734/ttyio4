import ttyio4 as ttyio

debug = False
done = False
pos = 0

prompt = "prompt: "
ttyio.echo(prompt, end="", flush=True)

buf = ""
while not done:
    ch = ttyio.getch(noneok=False)
#    ttyio.echo("ch=%r" % (ch))
    if ch == "":
        continue
    elif ch == "\n":
        break
    elif ch == "\004":
        ttyio.echo("{/all}EOF")
        break
    elif ch == "\007":
        ttyio.echo("{bell}", end="", flush=True)
        continue
    elif ch == chr(127):
        ttyio.echo(ch, flush=True, end="")
#        ttyio.echo("backspace, pos=%d" % (pos))
        if pos > 0:
            pos -= 1
            ttyio.echo(chr(8)+" "+chr(8), flush=True, end="")
            buf = buf[:len(buf)-1]
        else:
            ttyio.echo("{bell}", end="",flush=True)
            pos = 0
#        ttyio.echo("pos=%r" % (pos))
        continue
    elif ch == chr(21): # ^u
        ctrlu = ""
        while pos >= 0:
            ctrlu += chr(8)+" "+chr(8)
            pos -= 1
        buf = ""
        ttyio.echo(ctrlu, flush=True, end="")
        continue
    elif ch == "KEY_UP":
        pass
    elif ch == "KEY_DOWN":
        pass
    elif ch == "KEY_HOME":
        pass
    elif ch == "KEY_END":
        pass

    if len(ch) == 1:
        if debug is True:
            ttyio.echo("%s(%d)" % (ch, ord(ch)), end="",flush=True)
        else:
            ttyio.echo("%s" % (ch), end="",flush=True)
        buf += ch
        pos += 1
    else:
        ttyio.echo("%s" % (ch))

ttyio.echo("{f6}buf=%r" % (buf))
#    ttyio.echo("pos=%d" % (pos))
