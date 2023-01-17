from os import system
from time import sleep

import pyautogui

# variaveis
site = 'https://www.proeis.rj.gov.br/Default.aspx'
USERNAME = '50790323'
PASSWORD = 'fac50@D'

escolha = 2  # 1 duque 2 segurança

# abrir navegador e entrar no site
system('start chrome.exe')
pyautogui.click(278, 52, duration=0.8)
pyautogui.write(site)
pyautogui.press('enter')

# login
pyautogui.click(436, 386, duration=1)
pyautogui.click(425, 462, duration=0.2)

pyautogui.click(388, 432, duration=0.9)
pyautogui.write(USERNAME)
pyautogui.click(389, 503, duration=0.3)
pyautogui.write(PASSWORD)
pyautogui.click(433, 733, duration=0.2)
sleep(3)
pyautogui.click(378, 815)
pyautogui.click(429, 492, duration=0.8)
pyautogui.click(382, 434, duration=0.2)

if escolha == 1:
    pyautogui.click(420, 542, duration=0.4)
    pyautogui.press('m')
    pyautogui.press('m')
    pyautogui.press('m')
    pyautogui.press('enter')

elif escolha == 2:
    pyautogui.click(420, 542, duration=0.4)
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('enter')
