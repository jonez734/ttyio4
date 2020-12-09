from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str

def tokenize(buf):
    terminalwidth = 80

    # keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
#        ("F6",         r'{F6:(\d)}'),
        ("F6",         r'\{F6(:(\d))?\}'),
        ("WHITESPACE", r'[ \t\n]+'), # iswhitespace()
        ("COMMAND",    r'\{[^\}]+\}'),     # {red}, {brightyellow}, etc
        ("WORD",       r'[^ \t\n\{]+'),
        ('MISMATCH',   r'.')            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, buf):
        # print(mo)
        kind = mo.lastgroup
        value = mo.group()
        # column = mo.start() - line_start
        if kind == "WHITESPACE":
            pass
        elif kind == "COMMAND":
            pass
        elif kind == "WORD":
            pass
        elif kind == "F6":
            if mo.group(3) is None:
                value = 1
            else:
                value = int(mo.group(3))
        elif kind == 'MISMATCH':
            pass
            # raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value)

terminalwidth = 80
# buf = '''          {red}foo bar {green}baz     !{F6}here is another line{yellow}with a yellow ending.'''

buf = """{F6:2}     {white}Lorem ipsum dolor sit amet,{F6}consectetur adipiscing elit. Qu{blink}isqu{/blink}e ac risus tempor, {orange}porttitor diam id, ullamcorper ipsum. Maecenas quis sapien eget massa finibus auctor. Aliquam purus ligula, commodo ac tellus vitae, tincidunt molestie nisi. Duis dapibus sit amet enim laoreet rutrum. Nunc in sem posuere, tincidunt mi vitae, bibendum nisl. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Vestibulum molestie elementum sapien non consectetur. Praesent in auctor felis. Ut nec eros ac nunc porttitor aliquam id ornare ante. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer imperdiet id lorem sit amet sollicitudin. Maecenas sollicitudin efficitur leo, quis vulputate metus bibendum ornare. Fusce vel ex vehicula libero scelerisque lobortis. Etiam at nibh purus. Aliquam ac neque volutpat, condimentum nibh nec, eleifend dolor. Aenean feugiat, mauris at tempor convallis, leo neque feugiat arcu, sed tincidunt ipsum felis et ligula. Vivamus sed consectetur ipsum. Donec augue velit, maximus in libero accumsan, hendrerit blandit mauris. Nunc lobortis faucibus accumsan. Maecenas varius arcu ut bibendum ultrices. Sed semper scelerisque lorem, sed vulputate nisi rutrum at. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec et suscipit elit. Cras hendrerit mauris ut odio faucibus, eget maximus elit auctor. """

pos = 0
result = ""
for token in tokenize(buf):
    # print(token)
    # print("pos=%d" % (pos))
    if token.type == "F6":
        v = token.value if token.value is not None else 1
        print("v=%r" % (v))
        result += "\n"*v
        pos = 0
    elif token.type == "WHITESPACE":
        result += token.value
        pos += len(token.value)
    elif token.type == "COMMAND":
        result += "{command: %r}" % (token.value)
    elif token.type == "WORD":
        if pos+len(token.value) > terminalwidth-1:
            result += "\n"
            pos = len(token.value)
            result += token.value
        else:
            result += token.value
            pos += len(token.value)

print
print(result)
# print("result=%r" % (result))
