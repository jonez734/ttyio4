import time
import ttyio4

ttyio4.echo("{bell}")
time.sleep(1)
ttyio4.echo("{BELL:2}{lightred}foo!{/all}{bell:2}")
