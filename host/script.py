import add_pinout
from lib import *


def


if __name__ == "__main__":
    pinout = {}
    pinout.update(add_pinout.read_pins())
    print(pinout)
    for key in pinout:
        print pinout[key]

    pin = raw_input("Input here: ")
    #pin = '\'' + pin + '\''
    print pinout[pin]