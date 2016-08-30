#include <util/delay.h>
#include "DigitalIO.h"
#include "boards.h"
#include "TWI.h"
#include "Serial.h"

int main() {
	
	// LED blink, just to have a hardware proof that program was uploaded
    constexpr hal::DigitalIO pin(hal::bsp::pins::LED);
    pin.init(hal::DigitalIO::OUTPUT);
    pin.reset();
	_delay_ms(2500);
    pin.set();
	_delay_ms(500);

	// serial communication
	hal::Serial0::init(9600)
	

}
