A = []
B = []
C = []
for i in range(3):
    lista = []
    for j in range(3):
        x = int(input('Digite número inteiro para formar am matriz A: '))
        lista.append(x)
    A.append(lista)
for i in range(3):
    lista = []
    for j in range(3):
        x = int(input('Digite número inteiro para formar am matriz B: '))
        lista.append(x)
    B.append(lista)
for i in range(len(A)):
    lista = []
    for j in range(len(A[i])):
        soma = 0
        soma = A[i][j] + B[i][j]
        lista.append(soma)
    C.append(lista)
print('A matriz resultante da soma de A + B é: ',C)    
    

#N3
