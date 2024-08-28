matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i + j == 3:
            soma += matriz[i][j]
media = soma/4
print('A média da diagonal secundaria é: %.2f'%media)

#N1
