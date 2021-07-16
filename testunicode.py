import ttyio4 as ttyio

def main():
    ttyio.echo("{u:heart:10}{u:diamond:2}")
    ttyio.echo("{u:dv}{u:sv:42}")
    ttyio.echo("{u:heart}{u:diamond}{u:club}{u:spade}")
    ttyio.echo("{u:drdvcorner}{u:dhline:10}{u:dldvcorner}")
    ttyio.echo("{u:dvline}          {u:dvline}")
    ttyio.echo("{u:dvdhrtee}{u:dhline:10}{u:dvdhltee}")
    ttyio.echo("{u:dvshrtee}{acs:hline:10}{u:dvshltee}")
    ttyio.echo("{unicode:dvdrcorner}{u:dhline:10}{u:dvdlcorner}") # {unicode:dvdhcross}")
    return

if __name__ == "__main__":
    main()
