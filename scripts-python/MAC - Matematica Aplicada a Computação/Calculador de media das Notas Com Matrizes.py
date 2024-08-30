matriz = []
media = []

def mat(matriz):
    t = 1
    mnf = []
    materia = input ("Digite o nome da matéria! : ")
    mnf.append(materia)
    print("Adicione uma nota!")
    print("")
    nota = float(input("Digite a nota! : "))
    print("-----------------------------------")
    mnf.append(nota)
    while t == 1:
        print("Deseja adicionar outra nota?")  
        print("Digite (1) para sim! Digite (0) para Não!")
        t = int(input ())
        if t == 1:
            nota = float(input("Digite a nota! : "))
            print("-----------------------------------")
            mnf.append(nota)
    matriz.append(mnf)

    x = 1
    while x == 1:
        print ("Deseja adicionar outra matéria?")
        print ("Digite (1) para sim! Digite (0) para Não!")
        x = int(input ())
        if x == 1:
            y = 1
            mn = []
            materia = input ("Digite o nome da matéria! : ")
            print("-----------------------------------")
            mn.append(materia)
            while y == 1:
                print("Deseja adicionar uma nota?")  
                print("Digite (1) para sim! Digite (0) para Não!")
                y = int(input ())
                if y == 1:
                    nota = float(input("Digite a nota! : "))
                    print("-----------------------------------")
                    mn.append(nota)
            matriz.append(mn)
    print("")
    print("Todas as notas")
    print("")
    for i in range (len (matriz)):   
        print(matriz[i])

def med(media):
    for i in range (len (matriz)):
        md = []
        soma = 0
        for j in range (len (matriz[i])):
            if j == 0:
                md.append(matriz[i][j])
            else:
                soma += (matriz[i][j])
        medi = soma/j
        md.append(medi)
        if medi >= 7:
            a = "Aprovado"
            md.append(a)
        else:
            b = "Reprovado"
            md.append(b)
        media.append(md)
    print("Media de cada disciplina")
    print("")
    for i in range (len (media)):   
        print(media[i])
        
cr = 0
def CRE (cr):
    for i in range (len (media)):   
        cr += media[i][1]
    cre = cr/ (i+1)
    print(" CRE do aluno:",n," é de --> CRE:",cre)


#MENU
print("CALCULADOR DE MÉDIA ESCOLAR!")
print("")
print("")
n = input("DIGITE SEU NOME : ")
print("")
print("")
mat(matriz)
print("")
print("")
med(media)
print("")
print("")
CRE(cr)




