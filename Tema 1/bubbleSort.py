sequencia = [4,2,4,7,19,50,1]

def trocar (seq,i):
    temp = seq[i]
    seq[i] = seq[i+1]
    seq[i+1] = temp

for x in range(0,len(sequencia)):
    for i in range(0,len(sequencia)-1):
        if sequencia[i] > sequencia[i+1]:
            trocar(sequencia,i)

print(sequencia)

for x in sequencia:
    print(x)


