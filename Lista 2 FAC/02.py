'''
Escrever um algoritmo que calcula o peso em determinado planeta

Code - PLanet - Gravity
1 - Mercurio  - 0,37
2 - Venus     - 0,88
3 - Marte     - 0,38
4 - Jupiter   - 2,64
5 - Saturno   - 1,15
6 - Urano     - 1,17

Formula: peso plaenta = (pesoterra/10) * gravidadeplaneta
'''
pesoTerra = input("Olá! Sou um programa que calcula o quanto você pesaria em outros planetas! Para Começar, insira seu peso:")
pesoTerra = int(pesoTerra)
code = 0
while code != 7:
    print("Digite o código do planeta:")
    print("1 - Mercurio")
    print("2 - Venus")
    print("3 - Marte")
    print("4 - Jupiter")
    print("5 - Saturno")
    print("6 - Urano")
    code = int(input("7 - Encerrar programa"))
    if code == 1:
        pesoPlaneta = (pesoTerra / 10) * 0.73
        print(f"Seu peso em Mercurio seria {pesoPlaneta::.2f}")
    elif code==2:
        pesoPlaneta = (pesoTerra / 10) * 0.88
        print(f"Seu peso em Venus seria {pesoPlaneta:.2f}")
    elif code==3:
        pesoPlaneta = (pesoTerra / 10) * 0.38
        print(f"Seu peso em Marte seria {pesoPlaneta:.2f}")
    elif code==4:
        pesoPlaneta = (pesoTerra / 10) * 2.64
        print(f"Seu peso em Jupiter seria {pesoPlaneta::.2f}")
    elif code==5:
        pesoPlaneta = (pesoTerra / 10) * 1.15
        print(f"Seu peso em Saturno seria {pesoPlaneta:.2f}")
    else:
        pesoPlaneta = (pesoTerra / 10) * 1.17
        print(f"Seu peso em Urano seria {pesoPlaneta:.2f}")