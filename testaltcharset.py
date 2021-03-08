import ttyio4 as ttyio
import bbsengine5 as bbsengine

# https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#designate-character-set
# ttyio.echo("\033(0l{white}qqqqq{lightblue}qqqqqq{lightred}qqqk\033(B abcdefg!{/all}")
ttyio.echo("{lightred}{acs:hline}{/all}this is a test")


bbsengine.title("lorem ipsum lorem ipsum")
