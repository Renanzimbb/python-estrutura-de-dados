nomes = ["Renan", "Jose", "Souza", "Linhares"]

print(nomes)
for nome in nomes:
    print(nome)

#Coloca nome no final da lista
nomes.append('da Silva')
print(nomes)

#Para remover elemento conhecido
nomes.remove('Souza')
print(nomes)

#outra forma de remover com pop de determinado índice conhecido

nomes.pop(2)
print(nomes)

x = 2*2**4
print(x)