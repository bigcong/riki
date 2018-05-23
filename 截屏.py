import time

import pymouse, pykeyboard, os, sys
from PIL import ImageGrab
from pymouse import *
from pykeyboard import PyKeyboard

k = PyKeyboard()

begin = int(time.time())
for i in range(10 ):
    time.sleep(1)
    im = ImageGrab.grab((800, 300, 2100, 600))
    w, h = im.size

    im.thumbnail((w // 2, h // 2))

    t = str(int(time.time() * 1000)) + '_' + str(int(time.time() ) - begin);
    im.save('data/' + t + ".png")

    k.press_key(" ")
