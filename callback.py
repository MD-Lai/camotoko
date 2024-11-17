# https://gpiozero.readthedocs.io/en/latest/
# Don't use RPi.GPIO, use gpiozero instead

import gpiozero
from signal import pause
import time

bounce_timer = {}

def button_callback(dev):
    print(f"pushed {dev} {time.time()}")
    # time.sleep(1)

if __name__ == "__main__":
    BUTTON_ID = 17
    button = gpiozero.Button(BUTTON_ID, bounce_time=0.002)
    # bounce_time is critical, without, it detects like,
    # every single bounce of the electrical contacts
    # and triggers an activation event multiple times.
    # It is something like a minimum required hold time + ignore time
    # setting it to 1 for example means the button has to be 
    # held down for at least 1 second to activate
    button.when_activated = button_callback
    
    pause()