import pyautogui

print("Press Ctrl+C to quit")

MOVEMENT = 50

try:
    while True:
        pyautogui.moveTo(pyautogui.position()[0]+MOVEMENT, pyautogui.position()[1], duration=1)
        pyautogui.moveTo(pyautogui.position()[0], pyautogui.position()[1]+MOVEMENT, duration=1)
        pyautogui.moveTo(pyautogui.position()[0]-MOVEMENT, pyautogui.position()[1], duration=1)
        pyautogui.moveTo(pyautogui.position()[0], pyautogui.position()[1]-MOVEMENT, duration=1)
except KeyboardInterrupt:
    print("Thank you for using KeepBusy")
