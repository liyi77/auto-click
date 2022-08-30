import pyautogui
import base
import json
import pyperclip

x ,y = base.get_initial_position('wechatauto.txt - Notepad')
field_data = {}
def report_health_info():
    with open("./JsonFormat.json", encoding="utf-8") as fn1: #json file path
        field_data = json.load(fn1)
    print(field_data)

    pyautogui.moveTo(25+x, 65+y, 0.5)
    pyautogui.click()

    pyperclip.copy(field_data['Name'])
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.typewrite(field_data['Identity'], 0.2)
