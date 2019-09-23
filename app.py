#!/usr/bin/env python
from scripts.pulse import pulse
from scripts.rainbow import rainbow
# from scripts.weather import weather
# from scripts.twitter import twitter
import blinkt

def lights():
    effect = rainbow
    effect()

if __name__ == '__main__':
    lights()
