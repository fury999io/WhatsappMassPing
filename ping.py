#!/bin/python3
# Developed by fury999
# https://github.com/fury999io
# After running the code, move the cursor immediately to the message box of the group chat. Wait till the last person of the group gets mentioned. Then move your mouse pointer towards a corner of the screen, the program would terminate.
import pyautogui, time

time.sleep(2)
i = 1
while True:
    pyautogui.typewrite("@")
    j = 0
    while j < i:
        pyautogui.press("down")
        j = j + 1
    pyautogui.press("enter")
    pyautogui.hotkey("shift", "enter")
    i = i + 1
