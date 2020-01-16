#!/usr/bin/env python

from datetime import date
from datetime import datetime
import time

import scrollphathd
from scrollphathd.fonts import font5x5

def diff_dates(date1, date2):
    return abs(date2-date1).days

def get_days():
    d1 = date(2020,12,25)
    d2 = date.today()
    result1 = diff_dates(d2, d1)
    return result1


# Uncomment the below if your display is upside down
#scrollphathd.rotate(degrees=180)

DISPLAY_BAR = True
BRIGHTNESS = 0.1
FONT = font5x5

# Auto scroll using a while + time mechanism (no thread)
while True:

    now = datetime.now

    # Every five minutes
    if (datetime.now().minute % 5 == 0):

        days = get_days()

        message = str(days)

        scrollphathd.write_string(message, brightness=BRIGHTNESS,font=FONT)

    else:

        # Display the time (HH:MM) in a 5x5 pixel font
        scrollphathd.write_string(
            time.strftime("%H:%M"),
            x=0,  # Align to the left of the buffer
            y=0,  # Align to the top of the buffer
            font=font5x5,  # Use the font5x5 font we imported above
            brightness=BRIGHTNESS  # Use our global brightness value
        )

        # int(time.time()) % 2 will tick between 0 and 1 every second.
        # We can use this fact to clear the ":" and cause it to blink on/off
        # every other second, like a digital clock.
        # To do this we clear a rectangle 8 pixels along, 0 down,
        # that's 1 pixel wide and 5 pixels tall.
        if int(time.time()) % 2 == 0:
            scrollphathd.clear_rect(8, 0, 1, 5)

    scrollphathd.show()

    # Wait for 0.1s
    time.sleep(0.1)

    scrollphathd.clear()

