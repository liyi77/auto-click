import pyautogui
import base
import time
# import json
# import pyperclip

x ,y = base.get_initial_position('疫测达')
# field_data = {}

def submit_once_student(count):
    # go to '复学申生康'
    pyautogui.moveTo(300+x, 330+y, 1)
    pyautogui.click()
    time.sleep(5)
    # go to '非本人'
    pyautogui.moveTo(340+x, 70+y, 1)
    pyautogui.click()
    # go to '信息选择'
    pyautogui.moveTo(390+x, 115+y, 1)
    pyautogui.click()
    # go to '姓名'
    while count > 0:
        count = count - 1
        pyautogui.moveTo(200+x, 550+y, 0.5)
        pyautogui.dragTo(200+x, 515+y, 0.5)
    # go to '确定'
    pyautogui.moveTo(380+x, 415+y, 1)
    pyautogui.click()
    # go to '下一步'
    pyautogui.moveTo(210+x, 745+y, 1)
    pyautogui.click()
    time.sleep(2)
    # go to '用户须知'
    pyautogui.moveTo(25+x, 550+y, 1)
    pyautogui.click() 
    # go to '确认提交'
    pyautogui.moveTo(210+x, 745+y, 1)
    pyautogui.click()
    time.sleep(2)
    # go to '首页'
    # pyautogui.moveTo(210+x, 315+y, 1)
    # pyautogui.click()
    # time.sleep(2)

def report_health_info(): 
    # with open("./JsonFormat.json", encoding="utf-8") as fn1: #json file path
    #     field_data = json.load(fn1)
    # print(field_data)

    # pyperclip.copy(field_data['Name'])
    # pyautogui.hotkey('ctrl', 'v')
    submit_once_student(0)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # submit_once_student(1)
    # pyautogui.typewrite(field_data['Identity'], 0.2)
