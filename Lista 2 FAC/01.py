#calcuadora de IMC em python
'''O IMC (Índice de Massa Corporal)
é um critério da Organização Mundial de Saúde
para dar uma indicação sobre a condição de
peso de uma pessoa adulta. A fórmula é:
IMC = peso / altura2

Elabore um algoritmo que, dados o peso e a
altura de um adulto, determine a sua condição
de acordo com a tabela abaixo:
IMC em adultos Condição
IMC < 18,5 Abaixo do peso
18,5 ≤ IMC < 25,0 Peso ideal
25,0 ≤ IMC < 30,0 Sobrepeso
30,0 ≤ IMC < 35,0 Obesidade grau I
35,0 ≤ IMC < 40,0 Obesidade grau II
IMC ≥ 40,0 Obesidade grau III'''

peso = input("Olá! Por favor, digite seu peso: ")
peso = float(peso)
altura = input("OK, digite sua altura em m: ")
altura = float(altura)

IMC = peso/(altura*altura)
IMC = int(IMC)

if IMC < 18.5:
    print(f"Você está abaixo do peso, seu IMC é: {IMC}")
elif IMC < 25.0:
    print(f"Você está no peso ideal! Seu IMC é: {IMC}")
elif IMC < 30.0:
     print(f"Você está em sobrepeso! Seu IMC é: {IMC}")
elif IMC < 35:
     print(f"Você está com obesidade grau I! Seu IMC é: {IMC}")
elif IMC < 40.0:
     print(f"Você está com obesidade grau II! Seu IMC é: {IMC}")
else:
     print(f"Você está com obesidade grau III! Seu IMC é: {IMC}")