from lib import *


def send_cmd(board, pinout, cmd):
    print cmd
    try:
        if cmd[0][:4] == 'LCL_':
                gpio_pin = GPIO(board, pinout[cmd[0]], GPIO.Mode.OUTPUT)
                if cmd[1] is '1': gpio_pin.write(True)
                elif cmd[1] is '0': gpio_pin.write(False)
                else: error()
        elif cmd[0] == 'WRITE':
            i2c_master.data_transfer(0x1E, cmd[1], len(cmd[1]))
            print i2c_slave.read()
    except KeyError:
        print 'Such pin does not exist.'
    except IndexError:
        print 'Not enough arguments.'