def insereOrdenada(k, L, n):
    i = 0  # início da busca da posição
    posInsercao = -1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                return -1  # erro, chave já existe
            else:
                posInsercao = i  # posição achada
                i = n + 1  # sair do laço
        else:
            i = i + 1  # continuar busca
        if i == n:
            posInsercao = n  # inserção no final da lista
        # final da busca de posição

    #empurra elementos para frente
    L.append('')  # aumenta um índice na lista
    i = n  # inicio do ajuste da lista
    while (i > posInsercao):
        L[i] = L[i - 1]  # empurra cada nó para o final
        i = i - 1
    L[posInsercao] = k  # insere novo nó
    return posInsercao  # saída normal da função


numeros=[1,2,3,4,6,7,8,9,10]
print(numeros)
insereOrdenada(5,numeros,len(numeros))
print(numeros)


def removeL(k, L, n):
    i = 0  # início da busca do nó
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i  # chave encontrada
            i = n + 1  # sair do laço
        else:
            i = i + 1  # continuar busca
    if i == n:
        return -1  # erro, chave não existe
        # final da busca do nó
    i = posRemocao  # início do ajuste da lista
    while (i < n - 1):
        L[i] = L[i + 1]  # puxa cada nó posterior 1 posição
        i = i + 1
    L.pop(n - 1)  # ajusta o tamanho da lista
    return posRemocao  # saída normal da função


def buscaOrdenada(k, L, n):
    i = 0
    indiceL = -1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                indiceL = i  # chave encontrada
                i = n + 1  # sair do laço
            else:
                i = n + 1  # chave>k, sair do laço
        else:
            i = i + 1  # continuar busca


    return indiceL  # -1 indica chave não achada

numeros=[1,2,3,4,6,7,8,9,10]
i=buscaOrdenada(5,numeros,len(numeros))
print (i)
i=buscaOrdenada(3,numeros,len(numeros))
print(i)