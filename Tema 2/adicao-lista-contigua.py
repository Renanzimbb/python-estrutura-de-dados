#inserção por função pronta append
teste = ['Joao', 'Maria', 'Anan']
teste.append('Mariazinha')
print(teste)


#aumento de lista dinamicamente, inserção no final
nomes = ['Joao', 'Maria', 'Anan']
def adicionarLista(k,L,n):
    L.append('')
    L[n] = k
    n+=1

adicionarLista('Cleo', nomes,len(nomes))
print(nomes)