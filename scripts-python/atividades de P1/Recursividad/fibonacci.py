def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Digite a posição da fibonacci: '))
n = n-1
print('numero correspondente a posição na fibonacci é:',fibonacci(n))

#N1
