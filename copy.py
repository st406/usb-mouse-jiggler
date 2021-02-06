import time
import board
from digitalio import DigitalInOut, Direction, Pull
import random
import usb_hid
from adafruit_hid.mouse import Mouse
 
mouse = Mouse(usb_hid.devices)

try:
	while True :
		x = random.randrange(-0.1, 0.1)
		mouse.move(x,0)
		time.sleep(30)
except KeyboardInterrupt:
    pass
