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

#Passo 3: 
pyautogui.click(x=432, y=364) #clica no doc
pyautogui.click(x=1160, y=183) #clica nos 3 pontinhos
pyautogui.click(x=932, y=632) #faz o download

#Passo 4:
import pandas as pd

tabela = pd.read_csv(r"C://home/natalie/Downloads/Compras.csv", sep=";")
print(tabela)
totalgasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
precoMedio = totalgasto / quantidade

#como fzr as coordenada do mouse:
#time.sleep(5)
#print(pyautogui.position())
