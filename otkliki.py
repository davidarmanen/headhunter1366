import pandas as pd
import pyautogui as pg
import pyclip
import keyboard
import time
import re
import sys

name = []
age = []
phone = []

def parse_otkliki():
    for i in range(100):
        pg.moveTo(497, 484)
        pg.click()
        pg.moveTo(889, 373)
        pg.click(clicks=3)
        pg.hotkey("ctrl", "c")
        time.sleep(1)
        name_data = str(pyclip.paste().strip(), "utf-8")
        name.append(name_data)
        pyclip.clear()
        pg.moveTo(404, 415)
        pg.doubleClick()
        pg.hotkey("ctrl", "c")
        time.sleep(1)
        age_data = str(pyclip.paste().strip(), "utf-8")
        age.append(age_data)
        pyclip.clear()
        pg.moveTo(354, 481)
        pg.click(clicks=3)
        pg.hotkey("ctrl", "c")
        time.sleep(1)
        phone_data = str(pyclip.paste().strip(), "utf-8")
        phone_data = re.sub('[^0-9]', '', phone_data)
        phone_data = phone_data.replace(" ", "")
        phone.append(phone_data)
        pyclip.clear()
        pg.hotkey("ctrl", "tab")
        data = {"name": name, "age": age, "phone": phone}
        df = pd.DataFrame(data)
        df.to_excel("E:/otklikihh.xlsx")


def stop_parse():
    sys.exit()


keyboard.add_hotkey('1', parse_otkliki)
keyboard.wait('3', stop_parse)



