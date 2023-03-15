import pyautogui
import time
pyautogui.PAUSE = 5

#Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa. O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.

#Passo 1: entrar no sistema da empresa
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter') #entrou no chrome, abriu nova guia e entrou no site da empresa

#Passo 2: fazer login
pyautogui.click(x=776, y=376)
pyautogui.write('namqsf@gmail.com')
pyautogui.click(x=717, y=460)
pyautogui.write('senha123')
pyautogui.click(x=693, y=515)

#como fzr as coordenada do mouse:
#time.sleep(5)
#print(pyautogui.position())
