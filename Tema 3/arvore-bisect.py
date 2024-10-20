import bisect


class Arvore(object):
    def __init__(self, elemento):
        self.arvore = []
        self.addElementos(elemento)

    # adicionar muitos elementos
    def addElementos(self, elemento):
        for i in elemento:
            if i in self: continue
            self.addElemento(i)

    # Adicionar um (1) elemento
    def addElemento(self, elemento):
        if elemento not in self:
            bisect.insort(self.arvore, elemento)

    # Remove um (1) elemento
    def removeElemento(self, elemento):
        try:
            self.arvore.remove(elemento)
        except ValueError:
            return False
        return True

    def __iter__(self):
          for element in self.arvore:
              yield element
    def __str__(self):
          return str(self.arvore)


if __name__ == '__main__':
    arvore = Arvore([12, 7, 7, 1, 3, 10])

print("árvore:", arvore)

print("Tem 7 na árvore?", 7 in arvore)

arvore.addElemento(4)
print("Adicionando 4: ", arvore)

arvore.removeElemento(3)
print("Removendo 3: ", arvore)

arvore.removeElemento(7)
print("Removendo 7: ", arvore)

arvore.addElementos([8, 40, 15, 68])
print("Adicionando vários elementos:", arvore)