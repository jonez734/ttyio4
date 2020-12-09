import ttyio4 as ttyio

buf = """{F6:2}     {white}Lorem {{ipsum}} dolor sit amet,{F6}consectetur
adipiscing elit.  Qu{blink}isqu{/blink}e ac risus tempor, {orange}porttitor
diam id, ullamcorper ipsum.  Maecenas quis sapien eget massa finibus auctor. 
Aliquam purus ligula, commodo ac tellus vitae, tincidunt molestie nisi. 
Duis dapibus sit amet enim laoreet rutrum.  Nunc in sem posuere, tincidunt
mi vitae, bibendum nisl.  Orci varius natoque penatibus et magnis dis
parturient montes, nascetur ridiculus mus.  Suspendisse potenti.  Vestibulum
molestie elementum sapien non consectetur.  Praesent in auctor felis.  Ut
nec eros ac nunc porttitor aliquam id ornare ante.  Orci varius natoque
{blue}penatibus et {red}magnis dis parturient montes, nascetur ridiculus mus.  Integer
imperdiet id lorem sit amet sollicitudin.  Maecenas sollicitudin efficitur
leo, quis vulputate metus bibendum ornare.  Fusce vel ex vehicula libero
scelerisque lobortis.  Etiam at nibh purus.  Aliquam ac neque volutpat,
condimentum nibh nec, eleifend dolor.  {yellow}Aenean feugiat, mauris at tempor
convallis, leo neque feugiat arcu, sed tincidunt ipsum felis et ligula. 
Vivamus sed consectetur ipsum.  Donec augue velit, maximus in libero
accumsan, hendrerit blandit mauris.  Nunc lobortis faucibus accumsan. 
Maecenas varius arcu ut bibendum ultrices.  Sed semper scelerisque lorem,
sed vulputate nisi rutrum at.  Vestibulum ante ipsum primis in faucibus orci
luctus et ultrices posuere cubilia curae; Donec et suscipit elit.  Cras
hendrerit mauris ut odio faucibus, eget maximus elit auctor.  {/all}"""


ttyio.echo(buf, width=80)
