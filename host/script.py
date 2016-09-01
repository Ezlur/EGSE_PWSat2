import add_pinout, lib
from commands import send_cmd

pinout = {}

avr_board = lib.AVRClient('COM3', 250000)
avr_slave = lib.AVRClient('COM5', 250000)

i2c_master = lib.I2CMaster(avr_board)
i2c_device = lib.I2CDevice(avr_board, 0x1E)
i2c_slave = lib.I2CSlave(avr_slave, 0x1E)


def error():
    print('Not a viable command.')


if __name__ == "__main__":
    pinout.update(add_pinout.read_pins())
    print(pinout)
    while(True):
        send_cmd(avr_board, pinout, raw_input().split())