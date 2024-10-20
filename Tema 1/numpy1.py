import numpy as np

nomes = np.array(['Joãozim', 'Maria', 'Ana'])
print(nomes)

#Função copy cria cópia do array que pode ser alterado, mas não altera o original
copia = nomes.copy()
copia[0] = 'Renan'
print(copia)

#Também cria uma cópia, mas qualquer mudança reflete no array original
visao = nomes.view()
visao[0] = 'Douglas'
print(visao)
print(nomes)

#A função enumerate() em Python é usada para iterar sobre uma sequência (como uma lista) ao mesmo tempo
# em que acompanha o índice de cada elemento

for indice, valor in enumerate(nomes):
    print(indice,valor)
    if valor == "Ana":
       nomes[indice] = 'Etz'

print(nomes)