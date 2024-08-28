print("A sequência de Fibonacci!")
n = int(input("Digite um número que represente a quantidade de termos que deseja mostrar: "))
primeiro = 0
anterior = 1
proximo = 1
soma = 0
if n >=1:
    print(primeiro)

    for i in range(n-1):
        print(anterior)
        soma = primeiro + anterior
        anterior = primeiro + proximo
        proximo = primeiro + soma + anterior
