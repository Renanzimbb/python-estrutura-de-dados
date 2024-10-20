from sbbst import sbbst

tree = sbbst()
nums = [131,4,134,135,10,1,3,21,14,142,80,146]
for num in nums:
    tree.insert(num)

print("Número de elementos:", tree.getSize())
print("altura:", tree.getHeightTree())
print("Min valor:", tree.getMinVal())
print("Max valor:", tree.getMaxVal())
print("3º menor valor:", tree.kthsmallest(3))
print("2º maior valor:", tree.kthlargest(2))
print("Pre-Orden:", tree.preOrder())
print("In-Ordem:", tree.inOrder())
print("Pos-Ordem:", tree.postOrder())
tree.delete(128)
tree.delete(3)
tree.insert(55)
print(tree)