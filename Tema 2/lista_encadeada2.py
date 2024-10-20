class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_no(self, chave, valor):
        novo_no = No(chave, valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            current = self.cabeca
            while current.proximo:
                current = current.proximo
            current.proximo = novo_no

    def imprimir_valores(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

    def busca(self, k):
        noAtual = self.cabeca
        if noAtual.chave == k:
            return noAtual  # chave encontrada
        while noAtual.proximo != None:
            noAtual = noAtual.proximo  # passe para próximo nó
            if noAtual.chave == k:
                return noAtual  # chave encontrada
        return None  # indica chave não achada

# Criando uma instância da lista encadeada
lista = ListaEncadeada()

# Adicionando nós à lista
lista.adicionar_no(1, "Valor 1")
lista.adicionar_no(2, "Valor 2")
lista.adicionar_no(3, "Valor 3")

# Imprimindo os valores da lista
lista.imprimir_valores()
teste = (lista.busca("Valor 3"))
print(teste)