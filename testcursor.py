import ttyio4 as ttyio

ttyio.echo("{cursorup:5}abcde{wait:1}", end="", flush=True)
ttyio.echo("{cursorright:15}fghijk{wait:1}", end="", flush=True)
ttyio.echo("{cursordown:10}lmnop{wait:1}", end="", flush=True)
ttyio.echo("{cursorleft:10}qrstuv{wait:1}", flush=True)
