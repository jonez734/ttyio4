buf = "this is a test of setting colors like {green}green{/green}, {yellow}yellow{/yellow}, and {autored}red{/autored}"

TOK_WORD =  0x0001
TOK_COLOR = 0x0002
TOK_CLS =   0x0003
TOK_RESET = 0x0004
TOK_EOW =   0x0005

tokenmapansi = (
    ("{autogreen}", "[autogreen]"),
    ("{autoyellow}", "[autoyellow]"),
    ("{autored}", "[autored]"),
    ("{home}", "[home]"),
    ("{cls}", "[cls]")
)

tokens = []

buf2 = ""
for b in buf:
    if b == TOK_EOW:
        tokens.append(TOK_EOW)
        continue
    elif b == "{":
        pass
print(tokens)
