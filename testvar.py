import ttyio4 as ttyio

ttyio.setvariable("test", 42)
# print (ttyio.getvariable("test"))
ttyio.echo("{var:test}{/all}")
