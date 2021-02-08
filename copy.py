import time
import board
import usb_hid
from adafruit_hid.mouse import Mouse
 
mouse = Mouse(usb_hid.devices)
y = 5
while True :
	mouse.move(0,y)
	y = y * -1
	time.sleep(5)
