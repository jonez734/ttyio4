import os, sys
import tty, termios, fcntl
import time
import select
import socket
import re

from typing import Any, List, NamedTuple

# @see http://www.python.org/doc/faq/library.html#how-do-i-get-a-single-keypress-at-a-time
# @see http://craftsman-hambs.blogspot.com/2009/11/getch-in-python-read-character-without.html
def getch() -> str:
  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)

  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
  try:
      while 1:
              try:
                r, w, x = select.select([fd],[],[],0.250)
              except socket.error as e:
                echo("%r: %r" % (e.code, e.msg), level="error")
                if e.args[0] == 4:
                  echo("interupted system call (tab switch?)")
                  continue
              if len(r) == 1:
                ch = sys.stdin.read(1)
                return ch
  finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
      print ("\033[0m", end="")

  return ch

# @see https://gist.github.com/sirpengi/5045885 2013-feb-27 in oftcphp sirpengi
# @since 20140529
# @since 20200719
def collapselist(lst):
    def chunk(lst):
        ret = [lst[0],]
        for i in lst[1:]:
            if ord(i) == ord(ret[-1]) + 1:
                pass
            else:
                yield ret
                ret = []
            ret.append(i)
        yield ret
    chunked = chunk(lst)
    ranges = ((min(l), max(l)) for l in chunked)
    return ", ".join("{0}-{1}".format(*l) if l[0] != l[1] else l[0] for l in ranges)

# @since 20201105
def inputchar(prompt:str, options:str, default:str="", opts:object=None) -> str:
  if opts is not None and opts.debug is True:
    echo("ttyio4.inputchar.100: options=%s" % (options), level="debug")
        
  default = default.upper() if default is not None else ""
  options = options.upper()
  echo(prompt, end="")
  sys.stdout.flush()

  while 1:
    ch = getch().upper()

    if ch == "\n":
      return default
      if default is not None:
        return default
      else:
        return ch
    elif ch in options:
      return ch

def accept(prompt:str, options:str, default:str="", debug:bool=False) -> str:
  if debug is True:
    echo("ttyio3.accept.100: options=%s" % (options), level="debug")
        
  default = default.upper() if default is not None else ""
  options = options.upper()
  echo(prompt, end="")
  sys.stdout.flush()

  while 1:
    ch = getch().upper()

    if ch == "\n":
      return default
      if default is not None:
        return default
      else:
        return ch
    elif ch in options:
      return ch

def inputboolean(prompt:str, default:bool=None) -> bool:
	ch = accept(prompt, "YNTF", default)
	if ch == "Y":
		echo("Yes")
		return True
	elif ch == "T":
		echo("True")
		return True
	elif ch == "N":
		echo("No")
		return False
	elif ch == "F":
		echo("False")
		return False

# https://www.c64-wiki.com/wiki/Color
# https://en.wikipedia.org/wiki/ANSI_escape_code
mcicommands = (
{ "command": "{clear}",      "ansi": "2J" },
{ "command": "{home}",       "ansi": "0;0H" },
{ "command": "{clreol}",     "ansi": "0K" },
{ "command": "{/all}",       "ansi": "0;39;49m" },
{ "command": "{/fgcolor}",   "ansi": "39m" },
{ "command": "{/bgcolor}",   "ansi": "49m" },

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
{ "command": "{bgblack}",      "ansi": "48;2;0;0;0m",       "rgb": (0,0,0) }, # 30m

{ "command": "{autowhite}",    "alias": "{bold}{white}"},
{ "command": "{autored}",      "alias": "{bold}{red}"},
{ "command": "{autocyan}",     "alias": "{bold}{cyan}"},
{ "command": "{autopurple}",   "alias": "{bold}{purple}"},
{ "command": "{autogreen}",    "alias": "{bold}{green}"},
{ "command": "{autoblue}",     "alias": "{bold}{blue}"},
{ "command": "{autoyellow}",   "alias": "{bold}{yellow}"},
{ "command": "{autoorange}",   "alias": "{bold}{orange}"},
{ "command": "{autobrown}",    "alias": "{bold}{brown}"},
{ "command": "{autogray}",     "alias": "{bold}{gray}"}
# { "command": "{autoblack}",      "alias": "{gray}"}
)

class Token(NamedTuple):
    type: str
    value: str

def __tokenizemci(buf:str):
    token_specification = [
        ("OPENBRACE",  r'\{\{'),
        ("CLOSEBRACE", r'\}\}'),
        ("F6",         r'\{F6(:(\d))?\}'),
        ("WHITESPACE", r'[ \t\n]+'), # iswhitespace()
        ("COMMAND",    r'\{[^\}]+\}'),     # {red}, {brightyellow}, etc
        ("WORD",       r'[^ \t\n\{\}]+'),
        ('MISMATCH',   r'.')            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, buf):
        kind = mo.lastgroup
        print("kind=%r mo.groups()=%r" % (kind, mo.groups()))
        value = mo.group()
        if kind == "WHITESPACE":
            pass
        elif kind == "COMMAND":
            pass
        elif kind == "WORD":
            pass
        elif kind == "F6":
          value = mo.group(2) or mo.group(5) or 1
        elif kind == 'MISMATCH':
            pass
            # raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value)

def __interpretmci(buf:str, width=None, stripcommands:bool=False, interpret=True, end="\n") -> str:
  if buf is None or buf == "":
    return ""

  if width is None:
    width = getterminalwidth()

  pos = 0
  result = ""
  for token in __tokenizemci(buf):
      # print(token)
      # print("pos=%d" % (pos))
      if token.type == "F6":
          v = token.value if token.value is not None else 1
          result += "\n"*v
          pos = 0
      elif token.type == "WHITESPACE":
          result += token.value
          pos += len(token.value)
      elif token.type == "COMMAND":
        if stripcommands is False:
          result += "{command: %r}" % (token.value)
      elif token.type == "WORD":
          if pos+len(token.value) >= width-1:
              result += "\n"
              pos = len(token.value)
              result += token.value
          else:
              result += token.value
              pos += len(token.value)
  
  return result

# copied from bbsengine.py
def echo(buf:str="", interpretmci:bool=True, stripcommands:bool=False, level:str=None, datestamp=False, end:str="\n", width:int=None, **kw):
  from dateutil.tz import tzlocal
  from datetime import datetime
  from time import strftime

  if width is None:
    width = getterminalwidth()
  
  if datestamp is True:
    now = datetime.now(tzlocal())
    stamp = strftime("%Y-%b-%d %I:%M:%S%P %Z (%a)", now.timetuple())
    buf = "%s %s" % (stamp, buf)

  if level is not None:
#    if level == "debug":
#      buf = "{autoblue}%s{/autoblue}" % (buf)
    if level == "warn":
      buf = "{autoyellow}%s{/autoyellow}" % (buf)
    elif level == "error":
      buf = "{autored}%s{/autored}" % (buf)
    elif level == "success":
      buf = "{autogreen}%s{/autogreen}" % (buf)
    buf += "{/all}"

  if interpretmci is True:
    buf = __interpretmci(buf, stripcommands=stripcommands, width=width, end=end)
  print(buf, end=end)
  return

# http://www.brandonrubin.me/2014/03/18/python-snippet-get-terminal-width/
# https://www.programcreek.com/python/example/1922/termios.TIOCGWINSZ
def getterminalwidth():
  from shutil import get_terminal_size

  res = get_terminal_size()
  return res.columns

  import subprocess

  command = ['tput', 'cols']

#  if sys.stdout.isatty() is False:
#    return False

  try:
    width = int(subprocess.check_output(command))
  except OSError as e:
    print("Invalid Command '{0}': exit status ({1})".format(command[0], e.errno))
    return False
  except subprocess.CalledProcessError as e:
    print("Command '{0}' returned non-zero exit status: ({1})".format(command, e.returncode))
    return False
  else:
    return width

# @see https://tldp.org/HOWTO/Xterm-Title-3.html
def xtname(name):
  if sys.stdout.isatty() is False:
    return False
  echo("\033]0;%s\x07" % (name))
  return

def handlemenu(opts, title, items, oldrecord, currecord, prompt="option", defaulthotkey=""):
    hotkeys = {}

    hotkeystr = ""

    for item in items:
        label = item["label"].lower()
        hotkey = item["hotkey"].lower() if item.has_key("hotkey") else None
#        ttyio.echo("hotkey=%s" % (hotkey), level="debug")
        if hotkey is not None and hotkey in label:
            label = label.replace(hotkey.lower(), "[{cyan}%s{/cyan}]" % (hotkey.upper()), 1)
        else:
            label = "[{cyan}%s{/cyan}] %s" % (hotkey, label)
        if item.has_key("key"):
            key = item["key"]
            if oldrecord[key] != currecord[key]:
                buf = "%s: %s (was %s)" % (label, currecord[key], oldrecord[key])
            else:
                buf = "%s: %s" % (label, currecord[key])
        else:
            buf = label
        
        hotkeys[hotkey] = item # ["longlabel"] if item.has_key("longlabel") else None
        if hotkey is not None:
            hotkeystr += hotkey
        echo(buf,datestamp=False)
    
    if currecord != oldrecord:
      echo("{yellow}** NEEDS SAVE **{/yellow}", datestamp=False)
    
    echo()
  
    ch = accept(prompt, hotkeystr, defaulthotkey)
    ch = ch.lower()
    longlabel = hotkeys[ch]["longlabel"] if hotkeys[ch].has_key("longlabel") else None
    if longlabel is not None:
        echo("{cyan}%s{/cyan} -- %s" % (ch.upper(), longlabel), datestamp=False)
    else:
        echo("{cyan}%s{/cyan}" % (ch.upper()), datestamp=False)
    return hotkeys[ch]

# @since 20170419
def inputdate(prompt, oldvalue=None, **kw):
  if oldvalue is not None:
    buf = inputstring(prompt, datestamp(oldvalue), **kw)
  else:
    buf = inputstring(prompt, **kw)
  epoch = getdate.getdate(buf)
  tz = LocalTimezone()
  stamp = datetime.fromtimestamp(epoch, tz)
  return stamp # datetime.fromtimestamp(epoch)

# @see https://stackoverflow.com/questions/9043551/regex-that-matches-integers-only
def inputinteger(prompt, oldvalue=None, mask="^([+-]?[1-9]\d*|0)$", verify=None, opts=None) -> int:
  oldvalue = int(oldvalue) if oldvalue is not None else ""
  buf = inputstring(prompt, oldvalue, mask=mask, verify=verify, opts=opts)

  if buf is None or buf == "":
    return None
  
  try:
    res = int(buf)
  except:
    return None
  else:
    return res

# @since 20110323
# @since 20190913
# @since 20200626
# @since 20200729
# @since 20200901
def inputstring(prompt:str, oldvalue:str=None, opts:object=None, mask=None, returnseq=False, **kw) -> str:
  import readline
  def preinputhook():
    readline.insert_text(str(oldvalue))
    readline.redisplay()

  if oldvalue is not None:
    readline.set_pre_input_hook(preinputhook)

  try:
    inputfunc = raw_input
  except NameError:
    inputfunc = input
  
  oldcompleter = readline.get_completer()
  olddelims = readline.get_completer_delims()

  multiple = kw["multiple"] if "multiple" in kw else None
  
  completer = kw["completer"] if "completer" in kw else None
  if completer is not None and callable(completer.completer) is True:
    if opts is not None and opts.debug is True:
      echo("setting completer function", level="debug")
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer.completer)
    if multiple is True:
      readline.set_completer_delims(", ")

  while True:
    try:
      prompt = handlemci(prompt)
      buf = inputfunc(prompt)
    except KeyboardInterrupt:
      echo("INTR")
      raise
    except EOFError:
      echo("EOF")
      raise
    finally:
      echo("{/all}") # print ("\x1b[0m", end="")

    if oldvalue is not None:
      readline.set_pre_input_hook(None)

    if buf is None or buf == "":
      if "noneok" in kw and kw["noneok"] is True:
        return None
      else:
        return oldvalue

    if mask is not None:
      if opts is not None and opts.debug is True:
        echo(re.match(mask, buf), level="debug")

      if re.match(mask, buf) is None:
        echo("{lightred}invalid input{/lightred}")
        echo()
        continue

    if multiple is True:
      completions = buf.split(",")
    else:
      completions = [buf]

    completions = [c.strip() for c in completions]

    if "verify" in kw and callable(kw["verify"]):
      verify = kw["verify"]
    else:
      result = buf
      break

    bang = []
    for c in completions:
      bang += c.split(" ")
    completions = bang
    validcompletions = []

    if opts is not None and opts.debug is True:
      echo("inputstring.200: verify is callable", level="debug")

    invalid = 0
    for c in completions:
      if verify(opts, c) is True:
        validcompletions.append(c)
      else:
        echo("%r is not valid" % (c))
        invalid += 1
        continue
    if invalid == 0:
      if opts.debug is True:
        echo("inputstring.220: no invalid entries, exiting loop")
      result = validcompletions
      break

  readline.set_completer(oldcompleter)
  readline.set_completer_delims(olddelims)

  if len(result) == 1 and type(result) == type([]) and returnseq==False:
    return result[0]
  return result

def inputboolean(prompt, options="YN", default=""):
  ch = accept(prompt, options, default)
  if ch == "Y":
    echo("Yes")
    return True
  elif ch == "T":
    echo("True")
    return True
  elif ch == "N":
    echo("No")
    return False
  elif ch == "F":
    echo("False")
    return False
  return None

def areyousure(prompt="are you sure? ", default="N", options="YN") -> bool:
  res = inputboolean(prompt, default=default, options=options)
  if res is True:
    return 0
  return 1

# @see https://stackoverflow.com/a/53981846
def readablelist(seq: List[Any], color:str="", itemcolor:str="") -> str:
    """Return a grammatically correct human readable string (with an Oxford comma)."""
    seq = [str(s) for s in seq]

    if len(seq) < 3:
      buf = "%s and %s" % (color, itemcolor)
      return buf.join(seq) # " and ".join(seq)

    buf = "%s, %s" % (color, itemcolor)
    return buf.join(seq[:-1]) + '%s, and %s' % (color, itemcolor) + seq[-1]

# @since 20200917
def detectansi():
  if sys.stdout.isatty() is False:
    return False

  stdinfd = sys.stdin.fileno()

  oldtermios = termios.tcgetattr(stdinfd)
  oldflags = fcntl.fcntl(stdinfd, fcntl.F_GETFL)

  newattr = termios.tcgetattr(stdinfd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(stdinfd, termios.TCSANOW, newattr)

  # fcntl.fcntl(stdinfd, fcntl.F_SETFL, oldflags)

  os.write(sys.stdout.fileno(), b"\033[6n")

  try:
    res = False
    for x in range(0, 8):
      ch = os.read(stdinfd, 1)
      if ch == b"\033":
        res = True
        break
  finally:
    termios.tcsetattr(stdinfd, termios.TCSAFLUSH, oldtermios)
    fcntl.fcntl(stdinfd, fcntl.F_SETFL, oldflags)
  return res

# @since 20201013
class genericInputCompleter(object):
  def __init__(self:object, opts:object, tablename:str, primarykey:str):
    self.matches = []
    self.dbh = bbsengine.databaseconnect(opts)
    self.debug = opts.debug
    self.tablename = tablename
    self.primarykey = primarykey

    if self.debug is True:
      ttyio.echo("init genericInputCompleter object", level="debug")

  @classmethod
  def getmatches(self, text):
    if self.debug is True:
      ttyio.echo("genericInputCompleter.110: called getmatches()", level="debug")
    sql = "select %s from %s where %s ilike %%s" % (self.primarykey, self.tablename, self.primarykey)
    dat = (text+"%",)
    cur = self.dbh.cursor()
    if self.debug is True:
      ttyio.echo("getmatches.140: mogrify=%r" % (cur.mogrify(sql, dat)), level="debug")
    cur.execute(sql, dat)
    res = cur.fetchall()
    if self.debug is True:
      ttyio.echo("getmatches.130: res=%r" % (res), level="debug")
    matches = []
    for rec in res:
      matches.append(rec[self.primarykey])

    cur.close()

    if self.debug is True:
      ttyio.echo("getmatches.120: matches=%r" % (matches), level="debug")

    return matches

  @classmethod
  def completer(self:object, text:str, state):
    if state == 0:
      self.matches = self.getmatches(text)

    return self.matches[state]

if __name__ == "__main__":
  print(inputchar("[A, B, C, D]", "ABCD", None))
