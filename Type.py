import time
import pyautogui

time.sleep(10)
text = open("Example.txt")
for each_line in text:
    time.sleep(0.3)
    pyautogui.typewrite(each_line)
