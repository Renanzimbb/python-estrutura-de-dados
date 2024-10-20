class No:
    def __init__(self,chave,valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaCircular:
    def __init__(self, cabeca=None):
        self.inicioLista = cabeca
        self.finalLista = cabeca
        self.finalLista.proximo = self.inicioLista
        self.inicioLista.anterior = self.finalLista

    def print(self):
        current = self.inicioLista
        while (current):
            print(current.valor)
            current = current.proximo

    def insereCircular(self, novoNo):
        if self.inicioLista == None:  # lista vazia
            self.inicioLista = novoNo
            self.finalLista = novoNo
            self.novoNo.proximo = self.inicioLista
            self.inicioLista.anterior = self.finalLista
        else:
            self.finalLista.proximo = novoNo  # insere o nó
            self.finalLista = novoNo  # atualiza ponteiros
            self.finalLista.proximo = self.inicioLista


b1 = No(1,"b")
b2 = No(1,"c")
teste = ListaCircular(b1)
teste.insereCircular(b2)
teste.print()