import pyautogui
import time
#é so trocar todos os time sleep por #pyautogui.PAUSE = 5

pyautogui.press('win')
time.sleep(5)
pyautogui.write('google chrome')
time.sleep(5)
pyautogui.press('enter')

time.sleep(5)
pyautogui.hotkey("ctrl", "t")
time.sleep(5)
pyautogui.write("https://youtu.be/b_CpWmkhwq0")
time.sleep(5)
pyautogui.press('enter')
