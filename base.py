import win32gui
import time
import sys

def get_initial_position(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd:
        x, y, right, bottom = win32gui.GetWindowRect(hwnd)
        return x, y
    else:
        print('no ' + window_name + ' found!\nsad goodbye :(')
        time.sleep(2)
        sys.exit()
