import add_pinout
from lib import *
#from commands import send_cmd

pinout = {}

avr_board = AVRClient('COM3', 250000)
avr_slave = AVRClient('COM5', 250000)

i2c_master = I2CMaster(avr_board)
i2c_slave_adress = 0x1E
i2c_device = I2CDevice(avr_board, i2c_slave_adress)
i2c_slave = I2CSlave(avr_slave, i2c_slave_adress) #TODO remove after debug


def error():
    print('Not a viable command.')


def setup():
    for pin in pinout:
        gpio_pin = GPIO(avr_board, pinout[pin], GPIO.Mode.OUTPUT)


def send_cmd(cmd):
    print cmd
    try:
        if cmd[0][:4] == 'LCL_':
            if cmd[0] == 'LCL_ALL':
                for pin in pinout:
                    gpio_pin = GPIO(avr_board, pinout[pin], GPIO.Mode.OUTPUT)
                    if cmd[1] = '1': gpio_pin.write(True)
                    elif cmd[1] is '0': gpio_pin.write(False)
                    else: error()
            else:
                gpio_pin = GPIO(avr_board, pinout[cmd[1]], GPIO.Mode.OUTPUT)
                if cmd[1] is '1': gpio_pin.write(True)
                elif cmd[1] is '0': gpio_pin.write(False)
                else: error()
        elif cmd[0] == 'WRITE':
            i2c_device.data_transfer(cmd[1], len(cmd[1]))
            print i2c_slave.read() #TODO remove after debug
        elif cmd[0] == 'READ':
            i2c_slave.buffer_tx_data('11001100') #TODO remove after debug
            print i2c_device.data_transfer([], len('1010')) #TODO find what len is ESP tx buffer
        elif cmd[0] == 'WRITE+READ':
            i2c_slave.buffer_tx_data([1,2,3,4,5]) #TODO remove after debug
            print i2c_device.data_transfer(cmd[1], len('1010')) #TODO find what len is ESP tx buffer
    except KeyError:
        print 'Such pin does not exist.'
    except IndexError:
        print 'Not enough arguments.'


if __name__ == "__main__":
    pinout.update(add_pinout.read_pins())
    print(pinout)
    while(True):
        send_cmd(raw_input().split())