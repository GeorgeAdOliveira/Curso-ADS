lista = []
comandos = ""
while(comandos != "fim" and comandos != "Fim"):
    comandos = input('Digite "Adicionar" para acrescentar algum item, "Remover" caso queira retirar algum item ou "fim" para encerrar o programa: ')
    while(comandos != "Adicionar" and comandos != "adicionar" and comandos != "Remover" and comandos != "remover" and comandos != "fim" and comandos != "Fim"):
        print("Comando inválido!")
        comandos = input('Digite "Adicionar" para acrescentar algum item, "Remover" caso queira retirar algum item ou "fim" para encerrar o programa: ')
    if(comandos == "Adicionar" or comandos == "adicionar"):
        processo = input("Informe um processo que queira adicionar à lista: ")
        lista.append(processo)     
    if(comandos == "Remover" or comandos == "remover"):
        if lista != []:
            print("O processo removido é:",lista[0])
            lista.pop(0)
    if(len(lista) == 0):
        print("A fila esta vazia")
    else:
        print("A fila é:",lista)
print("Programa encerrado!")
