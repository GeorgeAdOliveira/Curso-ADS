perguntas =  [[['O que é via láctea?', '(1)--> Marca de Leite', '(2)--> Civilização Antiga', '(3)--> Carro', '(4)--> Galáxia'],
               ['Quem compôs o hino da independência?', '(1)--> Dom Pedro I.', '(2)--> Manuel Bandeira', '(3)--> Castro Alves', '(4)--> Roberto Carlos'],
               ['Quingentésimo corresponde a qual número?','(1)--> 500', '(2)--> 5000', '(3)--> 50', '(4)--> 5'],
               ['Qual bicho transmite doença de chagas?', '(1)--> Abelha', '(2)--> barata', '(3)--> Pulga', '(4)--> Barbeiro'],
               ['Qual o primeiro dia da semana?','(1)--> Sabádo', '(2)--> Domingo', '(3)--> Segunda', '(4)--> Sexta ']],
              [['São exemplos de Sistema Operacionais:', '(1)--> Pacote Office', '(2)--> Android, Microsoft Windows,Linuse, MacOS ', '(3)--> Sistma de Backup', '(4)--> Software Antivirus'],
               ['Buscador da internet mais usado atualmente?', '(1)--> Yahoo', '(2)--> Instagram', '(3)--> Google', '(4)--> YouTube'],
               ['Quantos bits cabem em um byte?', '(1)--> 12 bits', '(2)--> 8 bits', '(3)--> 1 bit', '(4)--> 6 bits'],
               ['Quem pintou Mona Lisa?', '(1)--> Van Gogh', '(2)--> Pablo Picasso', '(3)--> Leonardo da Vinci', '(4)--> Salvador Dalí'],
               ['Qual o satélite natural da Terra?', '(1)--> Sol', '(2)--> Lua', '(3)--> Marte', '(4)--> Saturno']],
              [['N30??', '1', '2', '3', '4'],
               ['2??', '4', '5', '6', '7'],
               ['3??', '8', '9', '10', '11'],
               ['4??', '12', '13', '14', '15'],
               ['5??', '16', '17', '18', '19']],
              [['N40??', '1', '2', '3', '4'],
               ['2??', '4', '5', '6', '7'],
               ['3??', '8', '9', '10', '11'],
               ['4??', '12', '13', '14', '15'],
               ['5??', '16', '17', '18', '19']],
              [['N50??', '1', '2', '3', '4'],
               ['2??', '4', '5', '6', '7'],
               ['3??', '8', '9', '10', '11'],
               ['4??', '12', '13', '14', '15'],
               ['5??', '16', '17', '18', '19']]]


gabarito =    [['4', '1', '1', '4', '2'],  
               ['2', '3', '2', '3', '2'],
               ['4', '', '', '', ''],
               ['4', '', '', '', ''],
               ['4', '', '', '', '']]

# É A ALTERNATIVA CERTA E A OUTRA A ERRADA
gabaritoRemocao =[[[1,4],[1,4],[1,4],[2,4],[1,2]],
                  [[1,2],[2,3],[1,2],[2,3],[1,2]],
                  [[1,4],[1,4],[1,4],[2,4],[1,2]],
                  [[1,4],[1,4],[1,4],[2,4],[1,2]]]


def PerguntaRes(i,j):
    print(perguntas[i][j][0])    #(perguntas[nivel][linha][coluna])
    print(perguntas[i][j][1])    # i = Nivel
    print(perguntas[i][j][2])    # j = Linha
    print(perguntas[i][j][3])
    print(perguntas[i][j][4])

def ajuda(i,j):
    a = gabaritoRemocao[i][j][0]
    b = gabaritoRemocao[i][j][1]
    print(perguntas[i][j][0])
    print(perguntas[i][j][a])
    print(perguntas[i][j][b])

 
qtdTrocar = 3
qtdAjuda = 1
i = 0

def nivels(i,j, qtdTrocar, qtdAjuda, perguntas, gabarito, remocao):
    continua = True
    pediuAjuda=False
    
    while continua:
        correta = gabarito[i][j]

        #SELEÇÕES
        if i == 0:
            print('Primeira pergunta valendo R$1.000,00. Em caso de desistência R$500,00.')
        elif i == 1:
            print('Segunda pergunta valendo R$10.000,00. Em caso de desistência R$5.000,00.')
        elif i == 2:
            print('Terceira pergunta valendo R$100.000,00. Em caso de desistência R$50.000,00.')
        elif i == 3:
            print('Quarta pergunta valendo R$500.000,00. Em caso de desistência R$250.000,00.')
        print()

        if  pediuAjuda == False :
            PerguntaRes(i,j)
        elif pediuAjuda == True :
            ajuda(i,j)
            pediuAjuda = False
            
        print()
        print('(D)--> Desistência')        

        #CONDIÇÃO PARA VERIFICAR SE O JOGADOR VAI TROCAR A PERGUNTA
        if qtdTrocar >= 1:
            print('(0)--> Para trocar a pergunta')
        else:
            print('Você não pode mais trocar a pergunta')

        #CONDIÇÃO PARA VERIFICAR SE O JOGADOR PODE PEDIR AJUDA
        if qtdAjuda >= 1:
            print('(A)--> Ajuda')
        else:
            print('Você não pode mais pedir ajuda!')

        #RESPOSTA DO JOGADOR
        x = input('')
        
        #CONDIÇÃO PARA VERIFICAR SE JOGADOR OPTOU POR TROCAR
        if x == '0' and qtdTrocar != 0 :
            qtdTrocar -= 1
            print(qtdTrocar)
            j += 1
            continua = True
            pediuAjuda = False

        #CONDIÇÃO PARA VERIFICAR SE JOGADOR VAI DESISTIR
        if x.upper() == 'D'.upper() :
            #PEGAR VALOR DE ACORDO COM O NIVEL DE DESISTENCIA
            if i == 0:
                print('Por conta da desistência você ganhou R$500,00. Obrigado por participar!')
            elif i == 1:
                print('Por conta da desistência você ganhou R$5.000,00. Obrigado por participar!')
            elif i == 2:
                print('Por conta da desistência você ganhou R$50.000,00. Obrigado por participar!')
            elif i == 3:
                print('Por conta da desistência você ganhou R$250.000,00. Obrigado por participar!')
            continua = False

        #CONDIÇÃO PARA VERIFICAR SE JOGADOR PEDIU AJUDA
        if x.upper() == 'A'.upper() :
            if qtdAjuda > 0:
                qtdAjuda -= 1
                pediuAjuda= True
            
        #CONDIÇÃO PARA VERIFICAR SE A RESPOSTA ESTÁ CORRETA
        if x == correta:
            #trocar as mensagens
            if i == 0:
                print('Resposta certa! você ganhou R$1.000,00.')
            elif i == 1:
                print('Resposta certa! você ganhou R$10.000,00.')
            elif i == 2:
                print('Resposta certa! você ganhou R$100.000,00.')
            elif i == 3:
                print('Resposta certa! você ganhou R$500.000,00.')
            i += 1
            continua = True
            
        elif x != correta and x != '0' and x.upper() != 'D'.upper() and x.upper() != 'A'.upper():
                #trocar as mensagens
            if i == 0:
                print('Resposta errada! Você ganhou R$500,00.')
            elif i == 1:
                print('Resposta errada! Você ganhou R$5.000,00.')
            elif i == 2:
                print('Resposta errada! Você ganhou R$50.000,00.')
            elif i == 3:
                print('Resposta errada! Você ganhou R$250.000,00.')
            continua = False
        print()
        
        #CONDIÇÃO PARA IR AO NIVEL 5
        if i == 4:
            continua = False
            print('Quinto e último nível valendo R$1.000.000,00. Em caso de desistência R$500.000,00.')
            PerguntaRes(i,j)
            print('(D)--> Desistência')
            x = input('')
            if x.upper() == 'D'.upper():
                print('Por conta da desistência você ganhou R$500.000,00. Obrigado por participar!')
            if x == correta :
                print('Resposta certa! Parabéns você ganhou R$1.000.000,00.')
            elif x != correta and x.upper() != 'D'.upper(): 
                print('Resposta errada! Você ganhou R$250.000,00.')

#FUNÇÃO PRINT
def prints():
    for i in range(3):
        print()
        
#REGRAS
def regras():
    print('Começa-se: \n'
          'Nível 1--> Pergunta valendo R$1.000,00 \n'
          'Nível 2--> Pergunta valendo R$10.000,00 \n'
          'Nível 3--> Pergunta valendo R$100.000,00 \n'
          'Nível 4--> Pergunta valendo R$500.000,00 \n'

          '--> Caso erre a pergunta, receberá metade do valor; \n'
          '--> Caso acerte a pergunta, irá para etapa seguinte; \n'
          '--> Só poderá pular a pergunta 3 vezes; \n'
          '--> Em caso de desistência ganha metade do valor do nível. \n'

          'Nível 5--> Pergunta valendo R$1 Milhão \n'
          
          '--> Esse último nível não será possível pedir ajuda; \n'
          '--> Não poderá pular a pergunta; \n'
          '--> Caso erre a pergunta, receberá R$250.000,00; \n'
          '--> Caso acerte ganhará o R$1 Milhão; \n'
          '--> Em caso de desistência receberá R$500.000.')
    

    
#MENU

j = 0
if j == 5:
    j = 0
start = True               
while start:
    prints()
    print('                      Seja Bem Vindo ao Show do Milhão!  ')
    prints()
    a = input('                         Aperte *Enter* para iniciar    ')
    prints()
    b = input('Digite seu nome: ')
    print()
    b = input('Olá '+b+'! Deseja consultar as regras do jogo: (0)--> Não (1)--> Sim : ')   
    print()
    if b == '1' :
        regras()
    prints()
    a = input('                         Aperte *Enter* para jogar    ')
    prints()
    nivels(i, j, qtdTrocar, qtdAjuda, perguntas, gabarito, gabaritoRemocao)
    j += 1


