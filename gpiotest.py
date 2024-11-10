# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

from gpiozero import Button
import time

# Wire config 
"""
sd ..G................. usb
   .L..................
G = Ground
L = Live
"""

LISTEN_TO = 2
SUCCESS_TIME = 0.002

button = Button(LISTEN_TO)
last_pressed = time.time()

print(f"The stupidest game ever.\nTry to press the button twice with less than {SUCCESS_TIME} between to exit the program")

while True:
    button.wait_for_active()
    print(f"activated button{LISTEN_TO}")
    button.wait_for_inactive()
    print(f"deactivated button{LISTEN_TO}")
    press_gap = time.time() - last_pressed
    last_pressed = time.time()
    print(press_gap)
    if press_gap < SUCCESS_TIME:
        break

# this is not a good way to do it. It sucks