class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:

    def push(novoNo):
        global pilha
        global topoPilha
        global maxPilha

        if topoPilha== None:				         #pilha vazia
                pilha[0] = novoNo			         #insere o nó
                topoPilha=0			      	         #atualiza o topo da pilha
    #    elif (topoPilha=maxPilha-1):		         #pilha cheia
                return -1		          		     # -1 → erro de pilha cheia
        else:
                topoPilha=topoPilha+1			     #atualiza o topo da pilha
                pilha[topoPilha] = novoNo	  	     #insere o nó
        return  topoPilha				             #saída normal

    def pop():
        global pilha
        global topoPilha
        global maxPilha
        if topoPilha== None: 			       # erro -pilha vazia
            return  None			       # None indica erro pilha vazia
        else:
            k =pilha[topoPilha]	           # salva o nó removido
            if topoPilha==0:
                topoPilha=None	           #pilha vazia após remoção
            else:
                topoPilha=topoPilha-1	   #remove o nó
            return k	                   #retorne k=o nó consumido

