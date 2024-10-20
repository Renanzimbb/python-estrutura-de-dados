#O que é lista em alocação contígua?
#Uma lista (também chamada de lista linear) é um conjunto de itens organizados sequencialmente (também chamados de nós), que, geralmente, guardam alguma relação entre si. Nessa lista, existe um item inicial
# e todos os demais itens
# são precedidos por um item
#. Um nó é composto por campos que armazenam informações e um dos campos, geralmente, serve como identificador, sendo comumente chamado de chave.


class No:
	def __init__(self, chave, valor):
		self.chave = chave
		self.valor = valor
		self.proximo = None

class FilaEncadeada:
    def __init__(self,inicio=None):
        self.inicio = inicio
        self.final = inicio

    def removeFila():
        global inicioFila  # indica o acesso a variáveis globais
        global maxFila
        global finalFila
        global fila
        if inicioFila == None:  # fila vazia
            return None  # erro fila vazia
        k = fila[inicioFila]  # salva o nó removido
        if finalFila == inicioFila:
            inicioFila = None  # fila vazia após remoção
        else:
            inicioFila = (inicioFila + 1) % maxFila  # remove o nó
        return k  # retorne k=o nó consumido

    def insereFila(novoNo):
        global inicioFila  # indica o acesso a variáveis globais
        global maxFila
        global finalFila
        global fila


        if inicioFila == None:  # fila vazia
            fila[0] = novoNo  # insere o nó
            inicioFila = 0  # atualiza o início da fila

            finalFila = 0  # atualiza o final da fila
        elif (finalFila + 1) % maxFila == inicioFila:  # fila cheia
            return -1  # -1 indica erro de fila cheia
        else:
            finalFila = (finalFila + 1) % maxFila  # atualiza o final da fila
            fila[finalFila] = novoNo  # insere o nó
        return finalFila  # saída normal


    def busca(self, k):
        noAtual = self.inicio
        if noAtual.chave == k:
            return noAtual  # chave encontrada
        while noAtual.proximo != None:
            noAtual = noAtual.proximo  # passe para próximo nó
            if noAtual.chave == k:
                return noAtual  # chave encontrada
        return None  # indica chave não achada


    def print(self):
        current = self.inicio
        while (current):
            print(current.valor)
            current = current.proximo


