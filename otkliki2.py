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
    while True:
        pg.moveTo(497, 564)
        pg.click()
        time.sleep(0.4)
        pg.moveTo(889, 449)
        pg.click(clicks=3)
        pg.hotkey("ctrl", "c", interval=0.25)
        name_data = str(pyclip.paste().strip(), "utf-8")
        name.append(name_data)
        pyclip.clear()
        pg.moveTo(404, 499)
        pg.doubleClick()
        time.sleep(0.4)
        pg.hotkey("ctrl", "c", interval=0.25)
        age_data = str(pyclip.paste().strip(), "utf-8")
        age.append(age_data)
        pyclip.clear()
        pg.moveTo(354, 563)
        pg.click(clicks=3)
        time.sleep(0.4)
        pg.hotkey("ctrl", "c", interval=0.25)
        phone_data = str(pyclip.paste().strip(), "utf-8")
        phone_data = phone_data.replace("— предпочитаемый способ связи", "")
        phone_data = re.sub('[^0-9]', '', phone_data)
        phone_data = phone_data.replace(" ", "")
        phone.append(phone_data)
        pyclip.clear()
        data = {"name": name, "age": age, "phone": phone}
        df = pd.DataFrame(data)
        df.to_excel("E:/otklikihh.xlsx")
        pg.hotkey("ctrl", "tab", interval=0.25)

def stop_parse():
    sys.exit()


keyboard.add_hotkey('1', parse_otkliki)
keyboard.wait('3', stop_parse)



