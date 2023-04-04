# Developed by fury999
# github.com/fury999io
# pyautogui module must be installed
# After running the code, move the cursor immediately to the message box of the group chat. Wait till the last person of the group gets mentioned. Then move your mouse pointer towards the corner of the screen, the program would stop
import pyautogui, time
  
time.sleep(2)
pyautogui.typewrite("@")
pyautogui.press("enter")
while True:
	pyautogui.typewrite("@")
	pyautogui.press("down")
	pyautogui.press("enter")
	pyautogui.typewrite(" ")
