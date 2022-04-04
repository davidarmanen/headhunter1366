import pandas as pd
import pyautogui as pg
import pyclip
import keyboard
import time
import re

name = []
age = []
phone = []

show_contacts_x = 222
show_contacts_y = 516
copy_name_x = 206
copy_name_y = 403
copy_age_x = 126
copy_age_y = 447
copy_phone_x = 77
copy_phone_y = 515

sleep_time = 1

def parse_otkliki():
    while True:
        pg.moveTo(show_contacts_x, show_contacts_y)
        pg.click()
        pg.moveTo(copy_name_x, copy_name_y)
        pg.click(clicks=3)
        pg.hotkey("ctrl", "c")
        time.sleep(sleep_time)
        name_data = str(pyclip.paste().strip(), "utf-8")
        name.append(name_data)
        pyclip.clear()
        pg.moveTo(copy_age_x, copy_age_y)
        pg.doubleClick()
        pg.hotkey("ctrl", "c")
        time.sleep(sleep_time)
        age_data = str(pyclip.paste().strip(), "utf-8")
        age.append(age_data)
        pyclip.clear()
        pg.moveTo(copy_phone_x, copy_phone_y)
        pg.click(clicks=3)
        pg.hotkey("ctrl", "c")
        time.sleep(sleep_time)
        phone_data = str(pyclip.paste().strip(), "utf-8")
        phone_data = phone_data.replace("— предпочитаемый способ связи", "")
        phone_data = re.sub('[()+-]', '', phone_data)
        phone_data = phone_data.replace(" ", "")
        phone.append(phone_data)
        pyclip.clear()
        data = {"name": name, "age": age, "phone": phone}
        df = pd.DataFrame(data)
        df.to_excel("C:/Users/Admin/otklikihh.xlsx")
        pg.hotkey("ctrl", "tab", interval=0.25)
        time.sleep(sleep_time)

def stop_parse():
    sys.exit()


keyboard.add_hotkey('1', parse_otkliki)
keyboard.wait('3', stop_parse)



