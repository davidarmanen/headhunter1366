import sys
import pyautogui as pg
import keyboard
import time
import sys

color = (60, 157, 242)


def foo():
    s = pg.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pg.click(x1, y, button="middle")  # do something here
                return

def start():
    while True:
        try:
            foo()
            print("1231")
        except:
            pass1
        finally:
            pg.scroll(-600)
            time.sleep(0.5)


def stop():
    sys.exit()

keyboard.add_hotkey('1', start)
keyboard.wait('3', stop)
