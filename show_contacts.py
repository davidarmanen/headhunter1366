import sys
import pyautogui as pg
import keyboard
import time
import sys

def start():
    while True:
        try:
            coords = pg.locateOnScreen("show_contacts.png", confidence=0.9, region=(468, 196, 1920, 1080))
            coords = pg.center(coords)
            x, y = coords
            pg.click(x, y)
            pg.moveTo(x, y)
            pg.click(button="middle")
            pg.press("enter")
        except:
            pass
        finally:
            pg.scroll(-450)
            time.sleep(0.3)


def stop():
    sys.exit()

keyboard.add_hotkey('1', start)
keyboard.wait('3', stop)
