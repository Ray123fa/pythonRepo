import time
import pyautogui as pt

limit = input("Enter limit:")
message = input("Enter message:")
time.sleep(5)

for i in range(int(limit)):
	pt.typewrite(message)
	pt.press("enter")
	if i % 5 == 0:
		time.sleep(5)