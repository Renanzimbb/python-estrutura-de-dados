#Declarando matrizes como listas
amigos = [['Daniel',25,'Gêmeos'], ['Douglas',34,'Capricôrnio'], ['Maria', 43, 'Peixe'], ['Maria']]
print(amigos)

#Inserindo elementos na matriz
amigos.append(['Ana', 34, 'Virgem'])
print(amigos)

amigos[2].append('Juazeiro')
print(amigos)

#Removendo elementos da matriz
amigos[2].remove('Juazeiro')
print(amigos)

amigos.pop(0)
amigos[1].pop(1)
print(amigos)

#Iterando sobre a matriz
for x in amigos:
    print(x)

#Agora, para imprimir cada elemento em uma linha, você pode usar dois iteradores aninhados, como a seguir:
for x in amigos:
    #código só usa o iterador aninhado se o item de alto nível for uma lista, o que é checado usando-se a
    # função isinstance().
    if isinstance(x,list):
        for y in x:
            print(y)
    else:
        print(x)