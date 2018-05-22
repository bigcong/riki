from pynput.keyboard import Listener
import logging



def press(key):
    print(key)

with Listener(on_press = press) as listener:
        listener.join()