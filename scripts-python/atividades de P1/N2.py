matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
maior = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i != j:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

print('O maior número da matriz é:',maior)

#N2
