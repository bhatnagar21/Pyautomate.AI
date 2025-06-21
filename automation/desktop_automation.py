import pyautogui
import time
import subprocess

# Step 1: Open Notepad
subprocess.Popen("notepad.exe")
time.sleep(2)  # Wait for notepad to open

# Step 2: Type something
pyautogui.write("Hello, I am PyAutomate AI!", interval=0.1)
pyautogui.press("enter")
pyautogui.write("This is an automated desktop task.", interval=0.1)

# Step 3: Wait and then close
time.sleep(5)
pyautogui.hotkey('alt', 'f4')  # Close Notepad
time.sleep(1)
pyautogui.press('n')  # If 'Save changes' appears, press 'N'
