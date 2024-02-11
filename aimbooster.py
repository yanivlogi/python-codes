from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)
#Color of center: (252, 218, 194)
#       

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(0, 0, 2560,1440))

    width, height = pic.size

    for x in range(0, width, 4):
        for y in range(0, height, 4):

            r, g, b = pic.getpixel((x, y))

            if r == 0 and g == 0 and b == 0 :
                flag = 1
                click(x, y)
                time.sleep(0.06)
                break

        if flag == 1:
            break
