import ttyio4 as ttyio

# https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#designate-character-set
# ttyio.echo("\033(0l{white}qqqqq{lightblue}qqqqqq{lightred}qqqk\033(B abcdefg!{/all}")
ttyio.echo("{lightred}{acs:hline:10}{/all}this is a test")

