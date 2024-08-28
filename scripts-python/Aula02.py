#EX:01
x = int(input('Digite um valor: '))
if x > 0:
    print('Positivo')
elif x < 0:
    print('Negativo')
else :
    print('Neutro')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#EX:02
x = input('Digite uma letra do alfabeto: ')
if x == 'a':
    print('Vogal')
elif x == 'e':
    print('Vogal')
elif x == 'i':
    print('Vogal')
elif x == 'o':
    print('Vogal')
elif x == 'u':
    print('Vogal')
else:
    print('Consoate')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#EX:03
n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
maior = 0
menor = 0
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
elif n3 >= n1 and n3 >= n2:
    maior = n3
if n1 <= n2 and n1<= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
elif n3 <= n1 and n3 <= n2:
    menor = n3
print('Maior numero:',maior)
print('Menor numero:',menor)
