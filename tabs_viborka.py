import sys
import pyautogui as pg
import keyboard
import time

def start():
    while True:
        try:
            coords = pg.locateOnScreen("star.png", confidence=0.9, region=(326, 196, 1920, 1080))
            coords = pg.center(coords)
            x, y = coords
            pg.click(x+20, y, button="middle")
            pg.press("enter")
        except:
            pass
        finally:
            pg.scroll(-350)
            time.sleep(0.5)


def stop():
    sys.exit()

keyboard.add_hotkey('1', start)
keyboard.wait('3', stop)
