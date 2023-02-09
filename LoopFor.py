'''Faça um programa que leia um
número inteiro positivo N e exiba todos os
múltiplos de Y inferiores a N, onde N e Y são
fornecidos pelo usuário.'''

N = input('Digite um inteiro:')
N = int (N)
Y = input('Digite outro inteiro: ')
Y = int (Y)

for numero in range(1, N+1):
    if numero%Y==0:
        print(numero)