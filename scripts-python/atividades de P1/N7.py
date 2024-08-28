def A(x):
    A = ''
    for i in range(len(x)):
        A += (x[-(i+1)])
    return A     

def B(x):
    B = ''
    for i in range(len(x)//2 + len(x)%2):
        B += x[i]
    return B

def C(x):
    C = ''
    y = len(x)//2 + len(x)%2
    for i in range(len(x)//2 ):
        C += x[y]
        y += 1
    return C

def D(x):
    D = C(x) + B(x)
    return D

def E(x):
    vog ='aAeEiIoOuU'
    vogal = ''
    consoante = ''
    for i in range(len(x)):
        con = 1
        for j in range(len(vog)):
            if x[i] == vog[j]:
                vogal += x[i]
                con = 0
        if con == 1 :
            consoante += x[i]
    E = vogal + consoante
    return E

def F(x):
    F =''
    for i in range(len(x)//2):
        F += (B(x)[i])
        F += (C(x)[i])
    if len(x)%2 != 0:
        F += (B(x)[-1])
    return F

           
x = input('Digite uma palavra com tamanho minimo de 4 letras: ')
while len(x) < 4:
    x = input('A palavra não atingiu o tamanho minimo digite outra: ')
print('a.',A(x))
print('b.',B(x))
print('c.',C(x))
print('d.',D(x))
print('e.',E(x))
print('f.',F(x))

#N7
