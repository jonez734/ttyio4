import ttyio4 as ttyio

def main():
    ttyio.echo("{unicode:heart:10}{unicode:diamond:2}")
    ttyio.echo("{unicode:dv}{unicode:sv:42}")
    ttyio.echo("{unicode:heart}{unicode:diamond}{unicode:club}{unicode:spade}")
    ttyio.echo("{unicode:drdvcorner}{unicode:dhline:10}{unicode:dldvcorner}")
    ttyio.echo("{unicode:dvline}          {unicode:dvline}")
    ttyio.echo("{unicode:dvdhrtee}{unicode:dhline:10}{unicode:dvdhltee}")
    ttyio.echo("{unicode:dvshrtee}{acs:hline:10}{unicode:dvshltee}")
    ttyio.echo("{unicode:dvdrcorner}{unicode:dhline:10}{unicode:dvdlcorner}") # {unicode:dvdhcross}")
    return

if __name__ == "__main__":
    main()
