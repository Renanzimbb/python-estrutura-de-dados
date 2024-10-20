class NoArvore:
    def __init__(self, chave = None,esquerda=None,direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def BuscaBST(raiz, chave):
    if raiz == None or raiz == chave:
        return raiz
    else:
        if raiz.chave < chave:
            return BuscaBST(raiz.direita, chave)
        elif raiz.chave > chave:
            return BuscaBST(raiz.esquerda, chave)
        else:
            return raiz


def Prefixa(raiz):
    if raiz:
        print(raiz.chave)
        Prefixa(raiz.esquerda)
        Prefixa(raiz.direita)

def Infixo(raiz):
    if raiz:
        Infixo(raiz.esquerda)
        print(raiz.chave)
        Infixo(raiz.direita)

def Posfixo(raiz):
    if raiz:
        Posfixo(raiz.esquerda)
        Posfixo(raiz.direita)
        print(raiz.chave)

def VisitaPreOrdem(raiz):
    if raiz:
        print(raiz.chave, end=" ")
        VisitaPreOrdem(raiz.esquerda)
        VisitaPreOrdem(raiz.direita)

def VisitaInOrdem(raiz):
    if raiz:
        VisitaInOrdem(raiz.esquerda)
        print(raiz.chave, end=" ")
        VisitaInOrdem(raiz.direita)

def VisitaPosOrdem(raiz):
    if raiz:
        VisitaPosOrdem(raiz.esquerda)
        VisitaPosOrdem(raiz.direita)
        print(raiz.chave, end =" ")

def ImprimeArvoreRecurs(raiz, nivel=0):
    if raiz is not None:
        # Print the right child nodes first
        ImprimeArvoreRecurs(raiz.direita, nivel + 1)

        # Indent to the correct level before printing the current node
        print("   " * nivel, raiz.chave)

        # Print the left child nodes
        ImprimeArvoreRecurs(raiz.esquerda, nivel + 1)

def InserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.chave == chave:
            return raiz
        if raiz.chave > chave:
           raiz.esquerda = InserirBST(raiz.esquerda, chave)
        else:
            raiz.direita = InserirBST(raiz.direita, chave)
    return raiz

def DeleteBST(raiz, chave):
  if raiz is None:
      return NoArvore(chave)
  if chave < raiz.chave:
      raiz.esquerda = DeleteBST(raiz.esquerda, chave)
  elif(chave > raiz.chave):
      raiz.direita = DeleteBST(raiz.direita, chave)
  else:
      if raiz.esquerda is None:
         temp = raiz.direita
         raiz = None
         return temp
      elif raiz.direita is None:
         temp = raiz.esquerda
         raiz = None
         return temp
      temp = ValorNo(raiz.direita)
      raiz.chave = temp.chave
      raiz.direita = DeleteBST(raiz.direita, temp.chave)
  return raiz

def ValorNo(no):
    atual = no
    while(atual.esquerda is not None):
        atual = atual.esquerda
    return atual

if __name__ == "__main__":
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

#    raiz.direita.esquerda = NoArvore(65)
#   raiz.direita.direita = NoArvore(85)
#    raiz.esquerda.direita = NoArvore(25)
#    raiz.esquerda.esquerda = NoArvore(45)

    InserirBST(raiz,25)
    InserirBST(raiz,65)
    InserirBST(raiz, 45)
    InserirBST(raiz, 85)

    #DeleteBST(raiz,75)

    ImprimeArvoreRecurs(raiz)
    VisitaPreOrdem(raiz)
    print()
    VisitaInOrdem(raiz)
    print()
    VisitaPosOrdem(raiz)

