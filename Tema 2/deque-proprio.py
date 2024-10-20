class No:
    def __init__(self,chave,valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DequeEncadeada:
    def __init__ (self,inicio=None):
        self.inicio = inicio
        self.final = inicio

    def popBack(self):
        if self.final is None:
            return None
        else:
            k = self.final
            self.final = self.final.anterior
            self.final.proximo = None
            return k

    def popFront(self):
        if self.inicio is None:
            return None
        else:
            j = self.inicio
            self.inicio = self.inicio.proximo
            return j

    def insertFront(self, novoNo):
        if self.inicio is None:
            self.inicio = novoNo
            self.final = novoNo
            return None
        else:
            k = self.inicio
            self.inicio = novoNo
            self.inicio.proximo = k

    def insertBack(self, novoNo):
        if self.final is None:
            self.inicio = novoNo
            self.final = novoNo
            return None
        else:
            k = self.final
            self.final.proximo = novoNo
            self.final = novoNo
            self.final.anterior = k

    def print(self):
        current = self.inicio
        while(current):
            print(current.valor)
            current = current.proximo

if __name__ == "__main__":
    a1 = No(2,"b")
    a2 = No(3,"c")
    a3 = No(3,"d")
    a4 = No(10,"p")
    b1 = DequeEncadeada(a1)
    b1.insertFront(a2)
    b1.insertFront(a3)
    b1.insertBack(a4)
    b1.popBack()
    b1.print()
