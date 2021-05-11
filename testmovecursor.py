#!/usr/bin/env python

import sys
import time
import ttyio4 as ttyio
import bbsengine5 as bbsengine

terminalheight = ttyio.getterminalheight()

ttyio.echo("{DECSTBM:2,%d}" % (terminalheight-2))

terminalwidth = ttyio.getterminalwidth()
topstatus = "{bggray}{white}%s{/bgcolor}" % ("status here".ljust(terminalwidth))
ttyio.echo("{decsc}{home}%s{decrc}" % (topstatus), end="")
ttyio.echo("{blink}")
for x in range(0, 75):
    ttyio.echo("%s" % (str(x)), end="")
    topbar = "{bggray}{white}%s{/bgcolor}" % (str(x).ljust(terminalwidth))
    bbsengine.updatetopbar(topbar)
    #ttyio.echo("{DECSC}{HOME}{clreol}{white}{reverse}%s{/reverse}{decrc}" % (topstatus.ljust(terminalwidth)), end="")
    time.sleep(0.250)
#ttyio.echo("{decsc}{yellow}------------------------------cursor saved here")
# ttyio.echo("{DECSC}{CURPOS:0}cursor y is zero{DECRC}")
#ttyio.echo("{decrc}{lightred}cursor restored to here")
ttyio.echo("{reset}")
