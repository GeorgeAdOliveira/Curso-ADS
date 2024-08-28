caracteres = input("Digite uma string com ao menos 4 caracteres: ")
while(len(caracteres) < 4):
    print("A string não atingiu o tamanho mínimo necessário!")
    caracteres = input("Digite uma string com ao menos 4 caracteres: ")
#a
print(caracteres[::-1])
#b
print(caracteres[:(len(caracteres))//2:1])
#c
print(caracteres[(len(caracteres))//2:(len(caracteres)) :1])
#d
print((caracteres[(len(caracteres))//2:(len(caracteres)) :1])+(caracteres[:(len(caracteres))//2:1]))
#e
# to utilizando esse x na f pra facilitar a vida
x = caracteres
vogal = ''
consoante = ''
for i in range(len(caracteres)):
    if (x[i] == 'a' or x[i] == 'A' or x[i] == 'e' or x[i] == 'E' or x[i] == 'i' or x[i] == 'I' or x[i] == 'o' or x[i] == 'O' or x[i] == 'u' or x[i] == 'U'): 
        vogal += x[i]        
    else:
        consoante += x[i]
print(vogal + consoante)
#f
F =''
p1 = (caracteres[:(len(caracteres))//2:1])
p2 = (caracteres[(len(caracteres))//2:(len(caracteres)) :1])
for i in range(len(x)//2):
    F += (p1[i])
    F += (p2[i])
if len(x)%2 != 0:
    F += (p2[-1])
print(F)




