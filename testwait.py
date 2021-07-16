import ttyio4 as ttyio

# ttyio.echo("1{wait:1}2{wait:1}3{wait:3}")
ttyio.echo("4{wait:1}", end="", flush=True)
ttyio.echo("5{wait:2}", end="", flush=True)
ttyio.echo()
