import time
import board
from digitalio import DigitalInOut, Direction, Pull
import random
import usb_hid
from adafruit_hid.mouse import Mouse
 
mouse = Mouse(usb_hid.devices)

try:
	while True :
		x = random.randrange(-1, 1)
		y = random.randrange(-1, 1)
		mouse.move(x,y)
		time.sleep(30)
except KeyboardInterrupt:
    pass
