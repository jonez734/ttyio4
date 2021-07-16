# https://unicode.org/emoji/charts/full-emoji-list.html
# https://www.ascii-codes.com/
# https://en.wikipedia.org/wiki/Code_page_437
import ttyio4 as ttyio

# ttyio.echo(":100:")
buf = ""
for k in ttyio.emoji.keys():
    buf += "\"%s\": :%s: " % (k,k)
ttyio.echo(buf)
