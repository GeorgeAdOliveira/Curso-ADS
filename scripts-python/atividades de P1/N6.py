def primo(n):
    cont = 0
    for i in range(1,n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        primo = True
    else:
        primo = False
    return primo

n = int(input('Digite um número para verificar se ele primo ou não: '))
if primo(n) == True :
    print('O número %d é primo'%n)
elif primo(n) == False :
    print('O número %d não é primo'%n)


#N6
