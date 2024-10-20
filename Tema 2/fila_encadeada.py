class No:
	def __init__(self, chave, valor):
		self.chave = chave
		self.valor = valor
		self.proximo = None

class FilaEncadeada:
	def __init__(self,inicio=None):
		self.inicio = inicio
		self.final = inicio

	def insere(self, novoNo):
		if self.inicio == None:  # fila vazia
			self.inicio = novoNo  # atualiza o início da fila
			self.final = novoNo  # atualiza o final da fila
		else:
			self.final.proximo = novoNo  # insere o nó
			self.final = novoNo  # atualiza o final da fila

	def remove(self):
		if self.inicio == None:  # erro -fila vazia
			return None  # None indica erro fila vazia
		else:
			k = self.inicio  # salva o nó removido
			self.inicio = self.inicio.proximo  # remove o nó
			return k  # retorne k=o nó consumido


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


e0 = No(0,'Joao')
fila = FilaEncadeada(e0)
k0=fila.busca(0)
#print(k0.valor)
e1=No(1,'Maria')
fila.insere(e1)
e2=No(-1,'Ana')
fila.insere(e2)
e3=No(2,'Arthur')
fila.insere(e3)
fila.print()