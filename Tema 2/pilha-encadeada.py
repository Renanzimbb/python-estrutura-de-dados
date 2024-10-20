class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novoNo = No(valor)
        novoNo.proximo = self.topo
        self.topo = novoNo

    def pop(self):
        if self.topo is None:
            return None
        k = self.topo
        self.topo = self.topo.proximo
        return k.valor

if __name__ == "__main__":
    pilha = PilhaEncadeada()
    for i in range(10):
        pilha.push(i)
        print(f"Pushed {i}, Pilha: {pilha}")


