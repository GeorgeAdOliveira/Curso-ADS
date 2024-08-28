matri = int(input('Digite a matricula do vendedor: '))
prod1 = float(input('Digite o valor do 1° produto: '))
quant1 = int(input('Digite a quantidade do 1° produto: '))
prod2 = float(input('Digite o valor do 2° produto: '))
quant2 = int(input('Digite a quantidade do 2° produto: '))
prod3 = float(input('Digite o valor do 3° produto: '))
quant3 = int(input('Digite a quantidade do 3° produto: '))
total = prod1*quant1 + prod2*quant2 + prod3*quant3
comiss = total*0.12
print('A matricula do vendedor é: %d' %matri)
print('O total da compra é: %d' %total)
print('A comissão do vendedor será: %.2f' %comiss)
      


