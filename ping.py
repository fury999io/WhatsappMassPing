# Developed by fury999
# github.com/fury999io
# pyautogui module must be installed
# After running the code, move the cursor immediately to the message box of the group chat. Wait till the last person of the group gets mentioned. Then move your mouse pointer towards the corner of the screen, the program would stop
import pyautogui, time
  
time.sleep(2)
n=0
while True:
	i=0
	pyautogui.typewrite("@")
	while i<=n:
		pyautogui.press("down")
		i=i+1
	pyautogui.press("enter")
	n=n+1
 
