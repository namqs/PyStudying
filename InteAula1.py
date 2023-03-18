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

#Passo 5 e ultimo:
pyautogui.hotkey('ctrl', 't')
pyautogui.click(x=1162, y=166)
time.sleep(10)
pyautogui.click(x=120, y=206)
pyautogui.write('j')
time.sleep(4)
pyautogui.press('enter')
pyautogui.click(x=860, y=389)
pyautogui.write('Correio da programadora mais linda')
pyautogui.click(x=922, y=443)
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
texto = f''' 
Prezado,
Segue o relatório de compras
Total gasto: R$ {totalgasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço médio: R$ {precoMedio:,.2f}

Qualquer dúvida, me manda um zap.
Att., Natalie Marques.
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

#como fzr as coordenada do mouse:
#time.sleep(5)
#print(pyautogui.position())
