#Quando um array é criado, ele contém valores de determinado tipo. Se você criar um array com números inteiros,
# ele será de tipo inteiro. Da mesma forma, se você criar com strings, ele será automaticamente criado com strings.

# Você pode verificar o tipo de array com o comando arr.dtype:

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.dtype)

#Quando você cria o array, pode assinalar um tipo específico usando o comando dtype.
arr2 = np.array([1,2,3,4,5], dtype='S')
print(arr2.dtype)

#Ao usar o comando copy, você cria uma cópia do array.
# Qualquer alteração feita na cópia não afetará o valor do array original. Veja o código a seguir:

x = arr.copy()
x[0] = 42
print(x)
print(arr)

#Quando você usa o comando view, está usando outra variável para se referenciar ao mesmo array.
# Qualquer alteração feita em uma variável alterará o valor do array original.

y = arr.view()
y[0] = 43
print(y)
print(arr)

#Iterando sobre um array
for x in arr:
    print(x)

#A função enumerate() em Python é usada para iterar sobre uma sequência (como uma lista) ao mesmo tempo
# em que acompanha o índice de cada elemento
for indice,valor in enumerate(arr):
    print(indice, valor)