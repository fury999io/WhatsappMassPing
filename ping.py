# Developed by fury999
# github.com/fury999io
# After running the code, move the cursor immediately to the message box of the group chat. Wait till the last person of the group gets mentioned. Then move your mouse pointer towards a corner of the screen, the program would terminate.
import pyautogui, time
time.sleep(2)
pyautogui.typewrite("@")
pyautogui.press("enter")
pyautogui.hotkey('shift', 'enter')
while True:
	pyautogui.typewrite("@")
	pyautogui.press("down")
	pyautogui.press("enter")
	pyautogui.hotkey('shift', 'enter')
