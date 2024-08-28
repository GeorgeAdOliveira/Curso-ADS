nomes_produtos = [["maçã", "tomate", "alface", "cenoura","cebola", "uva", "limão", "coentro", "banana", "mamão"],
                  ["amaciante", "detergente", "desinfetante", "sabão em pó", "sabão em barra", "sabão líquido", "água sanitária", "limpa vidros", "multiuso", "alvejante"],
                  ["molho de tomate", "extrato de tomate", "molho shoyo", "molho caesar", "molho barbacue", "molho rosé", "molho quatro queijos", "molho bachamel", "molho italiano", "molho balsâmico"],
                  ["arroz", "feijão", "macarrão espaguete", "macarrão parafuso", "farinha de trigo", "massa para cuscuz", "massa para tapioca","açúcar", "sal", "café"],
                  ["shampoo", "condicionador", "sabonete", "pasta de dente", "escova de dente", "fio dental", "desodorante", "creme de cabelo", "absorvente", "sabonete líquido"],
                  ["água", "cerveja", "refrigerante", "suco", "vinho", "whisky", "cachaça", "vodka", "rum", "espumante"]]

valores = [[4.00, 6.00, 2.00, 3.00, 3.50, 4.50, 4.80, 1.00, 5.00, 6.20],
           [10.00, 8.00, 7.50, 5.30, 2.40, 8.30, 3.00, 11.00, 5.20, 12.00],
           [7.30, 8.30, 10.40, 18.00, 17.50, 18.70, 20.30, 20.30, 21.80, 10.20],
           [9.00, 8.00, 5.00, 5.40, 3.50, 2.30, 4.80, 10.10, 3.00, 9.70],
           [29.00, 32.00, 5.00, 2.50, 5.40, 1.30, 20.10, 25.40, 30.30, 34.80],
           [4.00, 6.80, 8.00, 11.00, 63.00, 100.00, 40.00, 75.00, 40.00, 80.00]]

carrinho = []
carrinho_quantidade = []
carrinho_valor = []
soma = 0

opcao = 0


def listar(x,y):
    for i in range(len(nomes_produtos[x])):
        print(i+y,"–",nomes_produtos[x][i],"– {:.2f}".format(valores[x][i]))

def listar_produtos():
    print("\nSupermercado Compre Mais")
    print("Lista de Produtos:")
    print("1 – Frutas e Verduras")
    print("2 – Produtos de Limpeza")
    print("3 – Molhos")
    print("4 – Alimentos")
    print("5 – Higiene Pessoal")
    print("6 – Bebidas")
    categoria = input("Escolha o número da categoria do produto desejado: ")
    if(categoria == "1"):
        print("\nFrutas e Verduras:")
        listar(0,1)
    elif(categoria == "2"):
        print("\nProdutos de Limpeza:")
        listar(1,11)
    elif(categoria == "3"):
        print("\nMolhos:")
        listar(2,21)
    elif(categoria == "4"):
        print("\nAlimentos:")
        listar(3,31)
    elif(categoria == "5"):
        print("\nHigiene Pessoal:")
        listar(4,41)
    elif(categoria == "6"):
        print("\nBebidas:")
        listar(5,51)
    else:
        print("Setor Inválido!")
    voltar_enter = input("Pressione Enter para voltar ao menu principal")

def add_carinho(x,y):
    carrinho.append(nomes_produtos[x][y])
    carrinho_valor.append(valores[x][y])

def adicionar_produto():
    resp = ""
    while(resp != "N"):
        num_produto = int(input("Número do produto: "))
        while(num_produto < 0 or num_produto > 60):
            num_produto = int(input("Número do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        if(num_produto < 11):
            add_carinho(0,num_produto - 1)
        elif(num_produto < 21):
            add_carinho(1,num_produto - 11)
        elif(num_produto < 31):
            add_carinho(2,num_produto - 21)
        elif(num_produto < 41):
            add_carinho(3,num_produto - 31)
        elif(num_produto < 51):
            add_carinho(4,num_produto - 41)
        elif(num_produto < 61):
            add_carinho(5,num_produto - 51)
        carrinho_quantidade.append(quantidade)
        resp = input("Deseja continuar? (S ou N): ").upper()
    voltar_enter = input("Pressione Enter para voltar ao menu principal")

def ver_carrinho():    
    if(len(carrinho) == 0):
        print("O carrinho está vazio!")
    else:
        for i in range(len(carrinho)):
            valor_total = carrinho_valor[i] * carrinho_quantidade[i]
            print(f"Nome do produto: {carrinho[i]}, Quantidade: {carrinho_quantidade[i]}, Valor: R${valor_total:.2f}")
    voltar_enter = input("Pressione Enter para voltar ao menu principal")


#MENU
while(opcao != "4"):
    print("\nMenu Inicial:")
    print("1 – Listar produtos")
    print("2 – Adicionar produto ao carrinho")
    print("3 – Ver carrinho")
    print("4 – Finalizar compra")
    opcao = input("Escolha o número da atividade do menu desejada: ")
    while(opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4"):
        opcao = input("Escolha o número da atividade do menu desejada: ")

    if(opcao == "1"):   #1 - listar produtos
        listar_produtos()

    elif(opcao == "2"):   #2 - adicionar produto ao carrinho
        adicionar_produto()
        
    elif(opcao == "3"):   #3 - ver carrinho
        ver_carrinho()
        

for i in range(len(carrinho)):  #4 - Finalizar compra
    soma += carrinho_valor[i] * carrinho_quantidade[i]
print("Finalizando compra...")
print(f"Valor total da compra: R${soma:.2f}")
