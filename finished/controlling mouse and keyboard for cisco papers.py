import pyautogui
import time

for i in range(22):
    # clicks next or begin assignment
    pyautogui.moveTo(179, 989)

    pyautogui.click()

    time.sleep(3)
    # copies the question
    pyautogui.moveTo(52, 248)

    pyautogui.tripleClick()

    pyautogui.rightClick()

    pyautogui.moveTo(59, 252)

    time.sleep(.5)

    pyautogui.click()

    time.sleep(.5)
    # paste the question in find box
    pyautogui.move(1414, 100)

    pyautogui.tripleClick()

    pyautogui.rightClick()

    pyautogui.moveTo(1486, 242)

    pyautogui.click()

    pyautogui.press('Enter')

    time.sleep(6)
