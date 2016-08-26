#include <util/delay.h>
#include "DigitalIO.h"
#include "boards.h"


int main() {
    constexpr hal::DigitalIO pin(hal::bsp::pins::LED);

    pin.init(hal::DigitalIO::OUTPUT);

    pin.reset();

    while (true) {
         pin.reset();
		_delay_ms(2500);
        pin.set();
		_delay_ms(500);
    }
}
