# Criar uma história genérica para que possa ser preenchida com dados em input
'''
Era uma vez uma pessoa chamada Aline. Ela tinha muitos sonhos e queria se mudar para Paris. Porém, para alcançar seus objetivos, ela precisaria 
de ajuda, pois era muito pobre e não sabia por onde começar. Foi aí que conheceu Clóvis, um garoto que possuia muitos sonhos também, porém, 
estava tão perdido quanto ela. Ela possuia 18 anos e ele 19, ambos residentes de uma pequena cidade do interior de Gurjão. Clóvis possuia ainda 
mais problemas, pois, além de nao saber por onde começar, era tremendamente ligado à sua cabra Vanessinha. Ele a ganhou quando tinha 3 aninhos,
 e adorava brincar e conversar com ela. Ligados por um sonho, Aline e Clóvis juntaram suas coisas e subiram em um(a) carroça para ir rumo à 
 João Pessoa, a fim de ganhar mais oportunidades para mudar de vida. E claro, Vanessinha foi junto. No meio da estrada eles encontraram Vando, 
 o fada madrinha do interior mais burro de todos! O que será que vem por ai? '''

#declarando variáveis com input pra interação com o usuário:
nome1 = input('Escolha um nome feminino: ')
lugar = input('Escolha um lugar bom: ')
nome2 = input('Escolha um nome masculo: ')
idadeEla = input('Selecione uma idade para a personagem feminina: ')
idadeEla = str(idadeEla) # transformando a variável do tipo int em uma string para poder ser exibido no print
idadeEle = input('Escolha uma idade para a personagem masculina: ')
idadeEle = str(idadeEle)
lugar2 = input('Escolha um nome para a cidade natal dos personagens: ')
animal = input('Selecione um animal feminino: ')
nome3 = input('Selecione um nome para seu animal: ')
ação1 = input('Adicione uma ação: ')
ação2 = input('Adicione mais uma ação: ')
transp = input('Selecione um meio de transporte: ')
lugar3 = input('Escreva o nome de um lugar: ')
nome4 = input('Escreva um nome masc: ')
adj = input ('Escolha um adjetivo ruim: ')



print ( 'Era uma vez uma pessoa chamada ' + nome1 + '. Ela tinha muitos sonhos e queria se mudar para ' + lugar + '.')
print ('Porém, para alcançar seus objetivos, ela precisaria de ajuda, pois era muito pobre e não sabia por onde começar. Foi aí que conheceu ')
print (nome2 + ', um garoto que possuia muitos sonhos também, porém, estava tão perdido quanto ela.')
print (' Ela possuia ' + idadeEla + ' anos e ele ' + idadeEle + ', ambos residentes de uma pequena cidade do interior de ' + lugar2 + '. ')
print (nome2 +' possuia ainda mais problemas, pois, além de nao saber por onde começar, era tremendamente ligado à sua ' + animal + ' ' + nome3 + '.')
print (' Ele a ganhou quando tinha 3 aninhos, e adorava ' + ação1 + ' e ' + ação2 + ' com ela. ')
print ('Ligados por um sonho, ' + nome1 + ' e ' + nome2 + ' juntaram suas coisas e subiram em um(a) ' + transp + ' para ir rumo à ' + lugar3 + ', a fim de ganhar mais oportunidades para mudar de vida.')
print ('E claro, ' + nome3 + ' foi junto. No meio da estrada eles encontraram ' + nome4 + ',  o fada madrinha do interior mais ' + adj + ' de todos! ')
print ('O que será que vem por ai?')