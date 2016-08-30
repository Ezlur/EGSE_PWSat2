pinout = dict.fromkeys([
        'LCL_3V3',
        'LCL_5V',
        'LCL_ACC',
        'LCL_RadFET+3V3',
        'LCL_CAMs+3V3',
        'LCL_SunS+3V3',
        'LCL_SENS+5v',
        'LCL_SAILmain',
        'LCL_SAILred',
        'LCL_SADSmain',
        'LCL_SADSred'
])

pin = 0


def is_pin_ok(pin):
    if pin == '0':
        print("That pin doesn't exist!")
        return False
    elif is_pin_taken(pin):
        print("That pin is already taken!")
        return False
    else:
        return True


def is_pin_taken(pin):
    for key in pinout:
        if pin == pinout[key]: return True
    return False


def write_pins():
    print("You can manually edit the pinout in \"pinout.txt\".")
    print("Write pin to which each line is connected:")

    for key in sorted(pinout.keys()):
        while True:
            pin = (input(key + ': '))
            if is_pin_ok(pin): break
        pinout[key] = pin

    with open("pinout.txt", 'w') as file:
        file.write(str(pinout))


if __name__ == "__main__":
    write_pins()