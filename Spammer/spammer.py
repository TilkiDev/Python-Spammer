import pyautogui, time 

time.sleep(5)

for word in open("yazi.txt","r"):
      pyautogui.typewrite(word)
      pyautogui.press("enter")