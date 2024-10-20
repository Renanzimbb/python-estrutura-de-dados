import numpy as np

matriz1=np.array([[1,2],[3,4],[5,6]])
matriz2=np.array([[7,8],[9,10],[11,12]])

matriz2=matriz1+matriz2
print(matriz2)

matriz2=matriz2-matriz1
print(matriz2)

#sum() que soma todos os elementos da matriz
print(matriz1.sum())

#max() que retorna o valor máximo
print(matriz1.max())

#min() que retorna o valor mínimo
print(matriz1.min())

#std() retornam a média e o desvio padrão, respectivamente
print(matriz1.std())

for indice,valor in enumerate(matriz1):
    print(matriz1[indice[indice]])
