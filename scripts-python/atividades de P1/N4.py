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

y = 0
for i in range(3):
    lista = []
    z = 0
    for i in range(len(A)):
        soma = 0
        for j in range(len(A[i])):
            soma += A[y][j] * B[j][z]
        z += 1
        lista.append(soma)
    y += 1  
    C.append(lista)
    
print('A matriz resultante da multiplicação de A * B é: ',C)    
    
#N4
