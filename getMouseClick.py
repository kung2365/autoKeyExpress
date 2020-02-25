from pynput import mouse
from functools import partial
import pyautogui
 
 
def foo():
    i = 0
    while True:
        i += 1
        print('click: {}'.format(i))
        print(pyautogui.position())
        yield
 
 
def on_click(x, y, button, pressed, foo):
    if pressed:
        next(foo)
 
 
bar = partial(on_click, foo=foo())
 
with mouse.Listener(on_click=bar) as listener:
    listener.join()