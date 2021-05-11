#!/usr/bin/env python

import re
import sys
import ttyio4 as ttyio
import bbsengine4 as bbsengine

def optimize(tokens):
  return tokens

#  return tokens
#  print(tokens)
  foo = []
  currentvalue = ""
  lasttoken = None
  for t in tokens:
    if t["token"] == "WHITESPACE": # and (lasttoken is not None and lasttoken["token"] == "WHITESPACE"):
      currentvalue += t["value"]
    else:
      if len(currentvalue) > 0:
        foo.append({"token": "WHITESPACE", "value": currentvalue})
        currentvalue = ""
      foo.append(t)
      currentvalue = ""
    lasttoken = t

#  print("foo=%r" % (foo))
  return foo

buf = """          {bgwhite}{red}Lorem {/all}{reverse}ipsum {blink}dolor{/blink} sit amet, consectetur {cyan}adipiscing elit,{/reverse} {purple}sed do eiusmod tempor incididunt ut labore{green} et dolore {blue}magna aliqua.  {yellow}Ut enim ad minim {orange}veniam, quis nostrud exercitation ullamco {brown}laboris nisi ut aliquip ex ea {lightred}commodo consequat.  Duis aute irure {gray}dolor in reprehenderit{/bold} in {strike}voluptate velit esse{/strike}
cillum dolore eu fugiat nulla pariatur.  {italic}Excepteur sint{/italic} occaecat {lightgreen}cupidatat non proident, sunt in {lightblue}culpa qui officia {underline}deserunt mollit anim id{/underline} minim veniam, {lightgray}quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat.  {bold}{green}Duis aute{/green}{/bold} irure dolor in reprehenderit in voluptate est laborum.{/all}"""

#print(ttyio.handlemci(buf))
#sys.exit(0)

buf = "{bggray}{white}posted on {yellow}2020-10-24 08:59pm EST{white} to {yellow}top.entertainment.comedy{white} and {yellow}top.entertainment.star_trek{white} by {yellow}jonez                                                                      "
buf += "{/all}"

tokens = ttyio.tokenizemci(buf)
print("tokens=%r" % (tokens))
tokens = ttyio.optimizemci(tokens)
print("-----")
print("optimized=%r" % (tokens))
print("-----")
print(ttyio.interpmci(tokens))
sys.exit(0)

#print("optimizing..")
#tokens = optimize(tokens)
#print
#print
#print(tokens)
#ttyio.echo(buf) # print(buf) # ttyio.echo(buf)
sys.exit(0)

print(ttyio.tokenizemci(buf))
sys.exit(0)

print("len=%s" % (len(buf)))
print
ttyio.echo(buf)
sys.exit(0)

print(len(buf))
print
tokens = ttyio.tokenizemci(buf)
print("before. tokens=%r" % (tokens))
print
newtokens = []

for t in range(0, len(tokens)-1):
  t1 = tokens[t]
  t2 = tokens[t+1]
  if t1["token"] == t2["token"]:
    t1["value"] += t2["value"]
    continue
    print("optimized")
print
print("after. tokens=%r" % (tokens))
print
sys.exit(0)
# buf = "{darkgray} {gray} {lightgray} {white}it is a new year.... {lightgray} {gray} {darkgray} {/all}"

buf = "{blue}{bold}{reverse}it is a new year...{/all} some other text"

# ttyio.echo(buf)


#ttyio.inputinteger("{yellow}prompt{cyan}: {green}")
#ttyio.echo("more foo bar")

#opts = {}

#bbsengine.title(opts, "bank", "cyan", "blue")

width = ttyio.getterminalwidth()-4
#foo = "bank"
#foo = "{bggray}{white}%s{/all}" % (foo.center(width))
#ttyio.echo(foo)

commandre = re.compile("\\{\\/?[^\\{]+\\}")#.match(s)
wordre = re.compile("([^\s\\{]+)")
emojire = re.compile(":([^\s]+):") # :lol:

ch = ttyio.inputchar("prompt: ", "ABCDE")
buf = "{autored}the quick brown fox jumps over the lazy dog{/all}"
sys.exit(0)
print(buf)
print
tokens = ttyio.tokenizemci(buf)
buf = ttyio.interpmci(tokens, interpret=False)
print(buf)
print
ttyio.echo(buf)
sys.exit(0)

buf2 = ttyio.interpetmcicommands(buf)
def handlemci(buf:str, stripcommands:bool=False) -> str:
  width = ttyio.getterminalwidth()
  # https://www.c64-wiki.com/wiki/Color
  # https://en.wikipedia.org/wiki/ANSI_escape_code
  mcicommands = (
  { "command": "{clear}",      "ansi": "2J" },
  { "command": "{home}",       "ansi": "0;0H" },
  { "command": "{clreol}",     "ansi": "0K" },
  { "command": "{/all}",       "ansi": "0m" },

  { "command": "{bold}",       "ansi": "1m" },
  { "command": "{/bold}",      "ansi": "22m" },
  { "command": "{faint}",      "ansi": "2m" },
  { "command": "{italic}",     "ansi": "3m" },
  { "command": "{/italic}",    "ansi": "23m" },
  { "command": "{underline}",  "ansi": "4m" },
  { "command": "{/underline}", "ansi": "24m" },
  { "command": "{blink}",      "ansi": "5m" },
  { "command": "{/blink}",     "ansi": "25m" },

  { "command": "{strike}",     "ansi": "9m" },
  { "command": "{/strike}",    "ansi": "29m" },

  { "command": "{magenta}",    "ansi": "35m" },

  { "command": "{reverse}",    "ansi": "7m" },
  { "command": "{/reverse}",   "ansi": "27m" },

  { "command": "{white}",      "ansi": "38;2;255;255;255m", "rgb": (255,255,255) }, # 37m
  { "command": "{red}",        "ansi": "38;2;136;0;0m",     "rgb": (136,0,0) }, # 31m
  { "command": "{cyan}",       "ansi": "38;2;170;255;238m", "rgb": (170,255,238) }, # 36m
  { "command": "{purple}",     "ansi": "38;2;204;68;204m",  "rgb": (204, 68, 204) }, # 35m
  { "command": "{green}",      "ansi": "38;2;0;204;85m",    "rgb": (0,204,85) }, # 32m
  { "command": "{blue}",       "ansi": "38;2;0;0;170m",     "rgb": (0,0,170) }, # 34m
  { "command": "{yellow}",     "ansi": "38;2;238;238;119m", "rgb": (238,238,119) }, # 33m
  { "command": "{orange}",     "ansi": "38;2;221;136;85m",  "rgb": (221,136,85) },
  { "command": "{brown}",      "ansi": "38;2;102;68;0m",    "rgb": (102,68,0) },
  { "command": "{lightred}",   "ansi": "38;2;255;119;119m", "rgb": (255, 119, 119) },
  { "command": "{darkgray}",   "ansi": "38;2;51;51;51m",    "rgb": (51, 51, 51) },
  { "command": "{gray}",       "ansi": "38;2;119;119;119m", "rgb": (119, 119, 119) },
  { "command": "{lightgreen}", "ansi": "38;2;170;255;102m", "rgb": (170, 255, 102) },
  { "command": "{lightblue}",  "ansi": "38;2;0;136;255m",   "rgb": (0, 136, 255) },
  { "command": "{lightgray}",  "ansi": "38;2;187;187;187m", "rgb": (187, 187, 187) },
  { "command": "{black}",      "ansi": "38;2;0;0;0m",       "rgb": (0,0,0) }, # 30m

  { "command": "{bgwhite}",      "ansi": "48;2;255;255;255m", "rgb": (255,255,255) }, # 37m
  { "command": "{bgred}",        "ansi": "48;2;136;0;0m",     "rgb": (136,0,0) }, # 31m
  { "command": "{bgcyan}",       "ansi": "48;2;170;255;238m", "rgb": (170,255,238) }, # 36m
  { "command": "{bgpurple}",     "ansi": "48;2;204;68;204m",  "rgb": (204, 68, 204) }, # 35m
  { "command": "{bggreen}",      "ansi": "48;2;0;204;85m",    "rgb": (0,204,85) }, # 32m
  { "command": "{bgblue}",       "ansi": "48;2;0;0;170m",     "rgb": (0,0,170) }, # 34m
  { "command": "{bgyellow}",     "ansi": "48;2;238;238;119m", "rgb": (238,238,119) }, # 33m
  { "command": "{bgorange}",     "ansi": "48;2;221;136;85m",  "rgb": (221,136,85) },
  { "command": "{bgbrown}",      "ansi": "48;2;102;68;0m",    "rgb": (102,68,0) },
  { "command": "{bglightred}",   "ansi": "48;2;255;119;119m", "rgb": (255, 119, 119) },
  { "command": "{bgdarkgray}",   "ansi": "48;2;51;51;51m",    "rgb": (51, 51, 51) },
  { "command": "{bggray}",       "ansi": "48;2;119;119;119m", "rgb": (119, 119, 119) },
  { "command": "{bglightgreen}", "ansi": "48;2;170;255;102m", "rgb": (170, 255, 102) },
  { "command": "{bglightblue}",  "ansi": "48;2;0;136;255m",   "rgb": (0, 136, 255) },
  { "command": "{bglightgray}",  "ansi": "48;2;187;187;187m", "rgb": (187, 187, 187) },
  { "command": "{bgblack}",      "ansi": "48;2;0;0;0m",       "rgb": (0,0,0) } # 30m
  )

  value = ""
  token = None
  nodes = []

  print(buf)
  print
  # 3 possible tokens: WORD, COMMAND, and WHITESPACE
  patterns = (commandre, wordre)
  index = 0
  for p in patterns:
    m = p.findall(buf)
    print("p=%r, m=%r" % (p, m))
  
  sys.exit(0)

  for ch in buf:
    # print("ch=%r value=%r" % (ch, value))
    if ch == "{":
      if len(value) > 0:
        nodes.append({"token":"WORD", "value":value})
        token = "COMMAND"
        value = ""
    elif ch == "}":
      nodes.append({"token":"COMMAND", "value":"{%s}" % (value)})
      value = ""
      token = None
    elif ch.isspace() is True:
      nodes.append({"token":"WORD", "value":value})
      nodes.append({"token":"WHITESPACE", "value":ch})
      value = ""
      token = None
    else:
      value += ch

  if len(value) > 0:
    nodes.append({"token":"WORD", "value":value})

  # nodes.append({"token": "COMMAND", "value":"{/all}"})

  buf = ""
  pos = 0
  for n in nodes:
    token = n["token"]
    value = n["value"]
    if token == "WORD":
      if len(value)+pos > width:
        pos = 0
        buf += "\n"
      else:
        pos += len(value)
        buf += value
    elif token == "WHITESPACE":
      buf += " "
      pos += 1
    elif token == "COMMAND":
      if stripcommands is False:
        value = value.lower()
        # print("value=%r" % (value))
        for item in mcicommands:
          command = item["command"]
          ansi = item["ansi"]
          if value == command:
            # print("value == k")
            buf += "\033[%s" % (ansi)
            break
    else:
      buf += value
  return buf

print (handlemci(buf))
