# Transformando os exemplos do exercicio anterior em formated strings

# 1 frase: Eu amo o João Lucas e somos um do outro há 1 ano, desde que a shark nos acolheu no nosso primeiro 25

emissor = 'eu'
quem = 'João Lucas'
tempo = 1
tempo = str(tempo)
quem2 = 'shark'
colocação = 'primeiro'
dia = 25
dia = str (dia)
texto = f'{emissor} amo o {quem} e somos um do outros há {tempo} ano, desde que a {quem2} nos acolheu no nosso {colocação} {dia}'

print ( )
print (texto) 

# 2 frase: 2024 é o ano que eu terminarei a faculdade de ADS, após 6 semestres mais um TCC com bem mais de 30 páginas

year = 2024
year = str (year)
quem = 'eu'
terminaroq= 'faculdade'
curso = 'ADS'
ndeSem = '6'
umOq = 'TCC'
nPaginas = 30
nPaginas = str (nPaginas)
texto2 = f'{year} é o ano que {quem} terminarei a {terminaroq} de {curso}, após {ndeSem} semestres mais um {umOq} com bem mais de {nPaginas} páginas'

print ( )
print (texto2) 

# 3 frase: João tem 1 cachorro chamado Zé, ele passeia 3 vezes por dia e faz 1 coco a cada passeio.
nome = 'João'
qnt = '1'
nome2 = 'Zé'
qnt2 = '3'
texto3 = f'{nome} tem {qnt} cachorro chamado {nome2}, ele passeia {qnt2} por dia e faz 1 coco a cada passeio.'

print ( )
print (texto3)

# 4 frase: Todo dia dou 5 reais aos meus 2 filhos, Camilo e Tryndashe, para comerem 1 salgado.

qnt = 5
qnt = str (qnt)
qnt2 = 2
qnt2 = str (qnt2)
nome = 'Camilo'
nome2 = 'Tryndashe'
qnt3 = 1
qnt3 = str (qnt3)
comida = 'salgado'
texto4 = f'Todo dia dou {qnt} reais aos meus {qnt2} filhos, {nome} e {nome2}, para comerem {qnt3} {comida}.'

print ( )
print (texto4)

# 5 frase: Sempre levo meus 2 cachorros, Mel e Jimmy, para passear 3 vezes por dia. 

qnt = '2'
nome = 'Mel'
nome2 = 'Jimmy'
qnt2 = '3'
texto5 = f'Sempre levo meus {qnt} cachorros, {nome} e {nome2}, para passear {qnt2} vezes por dia.'

print ( )
print (texto5)

# 6º frase: Quando João ia para a escola, pegava 2 ônibus na ida, e na volta 1 metrô

nome = 'João'
lugar = 'escola'
qnt = '2'
transp = 'ônibus'
qnt2 = '1'
transp2 = 'metrô'
texto6 = f'Quando {nome} ia para a {lugar}, pega {qnt} {transp} na ida, e na volta {qnt2} {transp2}'

print ()
print (texto6)

# 7 frase: Na casa de João moram 5 pessoas, e quando tem bolo, suas 2 irmãs comem tudo


lugar = 'casa'
nome = 'João'
qnt = '5'
comida = 'bolo'
qnt2 = '2'
quem = 'irmãs'
texto7 = f'Na {lugar} de {nome} moram {qnt} pessoas, e quando tem {comida}, suas {qnt2} {quem} comem tudo'

print ()
print (texto7)

# 8 frase: Ele ama a Natalie, eles tem 1 constelação juntos e ela é composta por 13 estrelas no céu.


nome = 'ele'
nome2 = 'Natalie'
qnt = '1'
objeto = 'constelação'
qnt2 = '13'
local = 'céu'
texto8 = f'{nome} ama a {nome2}, eles tem {qnt} {objeto} juntos e ela é composta por {qnt2} estrelas no {local}.'

print ()
print (texto8)
# 9º frase: Agosto é o melhor mês para Natalie, possui 31 dias e o aniversário dela é no dia 30.

mês = 'Agosto'
nome = 'Natalie'
qnt = '31'
qnt2 = '30'
texto9 = f'{mês} é o melhor mês para {nome}, possui {qnt} dias e o aniversário dela é no dia {qnt2}.'

print ()
print (texto9)

# 10º frase: Python é uma ótima linguagem, a número 1.

ling = 'Python'
adj = 'ótima'
qnt = '1'
texto10 = f'{ling} é uma {adj} linguagem, a número {qnt}'

print ()
print (texto10)