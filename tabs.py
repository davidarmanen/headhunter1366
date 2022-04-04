import sys
import pyautogui as pg
import keyboard
import time
import sys

def start():
    while True:
        try:
            coords = pg.locateOnScreen("checkbox.png", confidence=0.9, region=(340, 196, 1920, 1080))
            coords = pg.center(coords)
            x, y = coords
            pg.click(x, y)
            pg.moveTo(x+20, y)
            pg.click(button="middle")
            pg.press("enter")
        except:
            pass
        finally:
            pg.scroll(-600)
            time.sleep(0.5)


def stop():
    sys.exit()

keyboard.add_hotkey('1', start)
keyboard.wait('3', stop)
