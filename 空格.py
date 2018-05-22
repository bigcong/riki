import time

import pymouse, pykeyboard, os, sys
from PIL import ImageGrab
from pymouse import *
from pykeyboard import PyKeyboard
k = PyKeyboard()

for i in range(10):
    time.sleep(1)
    im = ImageGrab.grab((800, 300, 2100, 600))
    w, h = im.size

    im.thumbnail((w // 4, h // 4))

    t = str(int(time.time() * 1000))
    im.save('data/'+t+".png")

    k.press_key(" ")


