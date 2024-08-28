A = []
B = []
C = []
for i in range(3):
    lista = []
    for j in range(3):
        x = int(input('Digite número inteiro pra formar a matriz A: '))
        lista.append(x)
    A.append(lista)
for i in range(3):
    lista = []
    for j in range(3):
        x = int(input('Digite número inteiro pra formar a matriz B: '))
        lista.append(x)
    B.append(lista)

lista = []    
for i in range(len(A)):
    soma = 0
    for j in range(len(A[i])):
        mult = 0
        mult = A[i][j] * B[j][i]
        soma += mult
    lista.append(soma)
        
print(lista)

#N4 da lista de matrizes e funções.
