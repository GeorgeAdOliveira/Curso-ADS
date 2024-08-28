                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            from tkinter import *
perguntas =  [[['O que é via láctea?', '(1)--> Marca de Leite', '(2)--> Civilização Antiga', '(3)--> Carro', '(4)--> Galáxia'],
               ['Quem compôs o hino da independência?', '(1)--> Dom Pedro I.', '(2)--> Manuel Bandeira', '(3)--> Castro Alves', '(4)--> Roberto Carlos'],
               ['Quingentésimo corresponde a qual número?','(1)--> 500', '(2)--> 5000', '(3)--> 50', '(4)--> 5'],
               ['Qual bicho transmite doença de chagas?', '(1)--> Abelha', '(2)--> barata', '(3)--> Pulga', '(4)--> Barbeiro'],
               ['Qual o primeiro dia da semana?','(1)--> Sabádo', '(2)--> Domingo', '(3)--> Segunda', '(4)--> Sexta ']],
              [['São exemplos de Sistema Operacionais:', '(1)--> Pacote Office', '(2)--> Android, Microsoft Windows,Linux, Mac ', '(3)--> Sistma de Backup', '(4)--> Software Antivirus'],
               ['Buscador da internet mais usado atualmente?', '(1)--> Yahoo', '(2)--> Instagram', '(3)--> Google', '(4)--> YouTube'],
               ['Quantos bits cabem em um byte?', '(1)--> 12 bits', '(2)--> 8 bits', '(3)--> 1 bit', '(4)--> 6 bits'],
               ['Quem pintou Mona Lisa?', '(1)--> Van Gogh', '(2)--> Pablo Picasso', '(3)--> Leonardo da Vinci', '(4)--> Salvador Dalí'],
               ['Qual o satélite natural da Terra?', '(1)--> Sol', '(2)--> Lua', '(3)--> Marte', '(4)--> Saturno']],
              [['Como se chamam as metades da Terra?', '(1)--> Hemisfério nordeste', '(2)--> Hemisfério leste e oeste', '(3)--> Hemisfério norte e sul', '(4)--> Hemisfério sul'],
               ['Como se chama a linha imaginária que divide a Terra ao meio?', '(1)--> Paralela', '(2)--> Equador', '(3)--> Trópico de capricornio', '(4)--> Trópico de câncer'],
               ['Qual o país mais populoso do mundo?', '(1)--> Brasil', '(2)--> Ásia', '(3)--> China', '(4)--> Rússia'],
               ['Quantos fusos horários existem no Brasil?', '(1)--> 1 Fuso horário', '(2)--> 3 Fuso horários', '(3)--> 2 Fuso horários', '(4)--> 4 Fuso horários'],
               ['Em que país foi detectado o primeiro caso de Covid-19?', '(1)--> China', '(2)--> Japão', '(3)--> Ásia', '(4)--> Rússia']],
              [['Qual o nome de um polígono de três lados?', '(1)--> Pentágono', '(2)--> Quadrilátero', '(3)--> Triângulo', '(4)--> Hexágono'],
               ['O que é um compasso?', '(1)--> Instrumento usado para medir o tamanho dos passos de uma pessoa', '(2)--> É uma trena com aproximadamente 3 metros de comprimento', '(3)--> Instrumento de desenho usado para traçar circunferências', '(4)--> Um medidor de pressão arterial'],
               ['O que é uma fração?', '(1)--> Uma divisão entre dois números inteiros', '(2)--> Uma figura geométrica com no minimo 2 lados', '(3)--> Uma coleção com no minimo 5 elementos', '(4)--> É uma parcela de um todo'],
               ['Jargão significa?', '(1)--> Um tipo de macacão', '(2)--> Uma medida de comprimento', '(3)--> Uma gíria profissional', '(4)--> Um recipiente'],
               ['Quem foi o primeiro presidente da Acadenia Brasileira de Letras?', '(1)--> Machado de Assis', '(2)--> Ruy Barbosa', '(3)--> Austregésio de Athayde', '(4)--> Fernando Magalhães']],
              [['Qual foi a primeira civilização do mundo a usar a escrita?', '(1)--> Maia', '(2)--> Sumérios', '(3)--> Astecas', '(4)--> Egípcios'],
               ['Em qual ano foi criado o SUS no Brasil?', '(1)--> 1980', '(2)--> 1990', '(3)--> 1986', '(4)--> 1988'],
               ['Qual o país que sediou á copa do mundo da FIFA no ano de 2002?', '(1)--> Brasil', '(2)--> Ásia', '(3)--> Rússia', '(4)--> Japão e Corea do Sul'],
               ['Quantos tipos de efeitos placebo existe?', '(1)--> 4 tipos', '(2)--> 3 tipos', '(3)--> 1 tipo', '(4)--> 2 tipos'],
               ['Quem foi a única pessoa na história a receber o Premio Nobel em áreas científicas diferentes?', '(1)--> Albert Einstein', '(2)--> Stephen Hawking', '(3)--> Mahatma Gandhi', '(4)--> Marie Curie']]]


gabarito =    [['4', '1', '1', '4', '2'],  
               ['2', '3', '2', '3', '2'],
               ['3', '2', '3', '4', '1'],
               ['3', '3', '4', '3', '1'],
               ['2', '3', '4', '4', '4']]

# É A ALTERNATIVA CERTA E A OUTRA A ERRADA
gabaritoRemocao =[[[1,4],[1,4],[1,4],[2,4],[1,2]],
                  [[1,2],[2,3],[1,2],[2,3],[1,2]],
                  [[1,3],[1,2],[1,3],[2,4],[1,2]],
                  [[3,4],[1,3],[1,4],[2,3],[1,2]]]


def PerguntaRes(i,j):
    print(perguntas[i][j][0])    #(perguntas[nivel][linha][coluna])
    print(perguntas[i][j][1])    # i = Nivel
    print(perguntas[i][j][2])    # j = Linha
    print(perguntas[i][j][3])    # numero = coluna
    print(perguntas[i][j][4])

def ajuda(i,j):
    a = gabaritoRemocao[i][j][0]
    b = gabaritoRemocao[i][j][1]
    print(perguntas[i][j][0])
    print(perguntas[i][j][a])
    print(perguntas[i][j][b])

 
qtdTrocar = 3
qtdAjuda = 1
i = 0     # i = NIVEL
j = 0     # j = PERGUNTA


def nivels(i,j, qtdTrocar, qtdAjuda, perguntas, gabarito, remocao):
    continua = True
    pediuAjuda=False
    while continua:
        correta = gabarito[i][j]

        #SELEÇÕES DE NÍVEL
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


        #CONDIÇÃO PARA VERIFICAR SE JOGADOR VAI DESISTIR
        if x.upper() == 'D'.upper() :
            #PEGAR VALOR DE ACORDO COM O NIVEL DE DESISTENCIA

            #Criação da "janela" em caso de desistência
            janela = Tk()
            janela.title("Jogo Do Milhão")
            janela.geometry("500x300")
            if i == 0:
                print('Por conta da desistência você ganhou R$500,00. Obrigado por participar!')
                texto_desistencia = Label(janela, text = "Por conta da desistência\n\n\n\nVocê ganhou R$500,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_desistencia.grid(column = 1, row = 0, padx = 150, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 0", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 1:
                print('Por conta da desistência você ganhou R$5.000,00. Obrigado por participar!')
                texto_desistencia = Label(janela, text = "Por conta da desistência\n\n\n\nVocê ganhou R$5.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_desistencia.grid(column = 1, row = 0, padx = 150, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 1", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 2:
                print('Por conta da desistência você ganhou R$50.000,00. Obrigado por participar!')
                texto_desistencia = Label(janela, text = "Por conta da desistência\n\n\n\nVocê ganhou R$50.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_desistencia.grid(column = 1, row = 0, padx = 150, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 2", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 3:
                print('Por conta da desistência você ganhou R$250.000,00. Obrigado por participar!')
                texto_desistencia = Label(janela, text = "Por conta da desistência\n\n\n\nVocê ganhou R$250.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_desistencia.grid(column = 1, row = 0, padx = 150, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 3", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            continua = False
            janela.mainloop()
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
            
        elif x != correta and x != '0' and x.upper() != 'D'.upper() and x.upper() != 'A'.upper():
                #trocar as mensagens
            janela = Tk()
            if i == 0:
                print('Resposta errada! Você ganhou R$500,00.')
                texto_resposta = Label(janela, text = "Resposta errada!\n\n\n\nVocê ganhou R$500,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 0", fg = "blue" ,font = "Times")
                texto_2 = Label(janela, text = "Erros: 1", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 1:
                print('Resposta errada! Você ganhou R$5.000,00.')
                texto_resposta = Label(janela, text = "Resposta errada!\n\n\n\nVocê ganhou R$5.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 1", fg = "blue" ,font = "Times")
                texto_2 = Label(janela, text = "Erros: 1", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 2:
                print('Resposta errada! Você ganhou R$50.000,00.')
                texto_resposta = Label(janela, text = "Resposta errada!\n\n\n\nVocê ganhou R$50.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 2", fg = "blue" ,font = "Times")
                texto_2 = Label(janela, text = "Erros: 1", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            elif i == 3:
                print('Resposta errada! Você ganhou R$250.000,00.')
                texto_resposta = Label(janela, text = "Resposta errada!\n\n\n\nVocê ganhou R$250.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 3", fg = "blue" ,font = "Times")
                texto_2 = Label(janela, text = "Erros: 1", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
            janela.mainloop()
            continua = False
        print()

        if j == 5:
            j = recursiva(j)
        
        #CONDIÇÃO PARA IR AO NIVEL 5
        if i == 4:
            correta = gabarito[i][j]
            continua = False
            print('Quinto e último nível valendo R$1.000.000,00. Em caso de desistência R$500.000,00.')
            print()
            PerguntaRes(i,j)
            print('(D)--> Desistência')
            x = input('')
            if x.upper() == 'D'.upper():
                janela = Tk()
                janela.title("Jogo Do Milhão")
                janela.geometry("500x300")
                texto_desistencia = Label(janela, text = "Por conta da desistência\n\n\n\nVocê ganhou R$500.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_1 = Label(janela, text = "Acertos: 4", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
                texto_desistencia.grid(column = 1, row = 0, padx = 150, pady = 10)
                janela.mainloop()
            if x == correta :
                #Tkinter 
                janela = Tk()
                janela.title("Jogo Do Milhão")
                janela.geometry("500x300")
                texto_resposta = Label(janela, text = "Parabéns, resposta certa!\n\n\n\n\nVocê ganhou R$1.000.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 5", fg = "blue", font = "Times")
                texto_2 = Label(janela, text = "Erros: 0", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
                janela.mainloop()
            elif x != correta and x.upper() != 'D'.upper():
                janela = Tk()
                janela.title("Jogo Do Milhão")
                janela.geometry("500x300")
                texto_resposta = Label(janela, text = "Resposta errada!\n\n\n\nVocê ganhou R$250.000,00\n\n\n\nObrigado por participar!", font = "Georgia")
                texto_resposta.grid(column = 1, row = 0, padx = 140, pady = 10)
                texto_1 = Label(janela, text = "Acertos: 4", fg = "blue" ,font = "Times")
                texto_2 = Label(janela, text = "Erros: 1", fg = "red", font = "Times")
                texto_1.grid(column = 1, row = 1, padx = 150, pady = 10)
                texto_2.grid(column = 1, row = 2, padx = 150, pady = 10)
                janela.mainloop()

#FUNÇÃO PRINT
def prints():
    for i in range(3):
        print()

#RECURCIVIDADE    
def recursiva(j):
    if j == 0:
        return j
    else:
        return recursiva(j-1)

        
#MENU

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
        #Criando á "janela", Label e text. #REGRAS
        janela_2 = Tk()
        janela_2.title("Regras Do Jogo")
        janela_2.geometry("700x500")
        texto_orientador_1 = Label(janela_2, text = "Regras", font = "Century")
        texto_orientador_2 = Label(janela_2, text = "Começa-se:\nNivel 1 -> Pergunta valendo R$1.000,00", font = "Georgia")
        texto_orientador_3 = Label(janela_2, text = "Nivel 2 -> Pergunta valendo R$10.000,00", font = "Georgia")
        texto_orientador_4 = Label(janela_2, text = "Nivel 3 -> Pergunta valendo R$100.000,00", font = "Georgia")
        texto_orientador_5 = Label(janela_2, text = "Nivel 4 -> Pergunta valendo R$500.000,00", font = "Georgia")
        texto_orientador_6 = Label(janela_2, text = "Caso erre a pergunta, receberá metade do valor;", font = "Georgia")
        texto_orientador_7 = Label(janela_2, text = "Caso acerta a pergunta, irá para etapa seguinte;", font = "Georgia")
        texto_orientador_8 = Label(janela_2, text = "Em caso de desistência ganha metade do valor do nível\nSó poderá pular a pergunta 3 vezes;", font = "Georgia")
        texto_orientador_9 = Label(janela_2, text = "\n Nivel 5 -> Pegunta valendo R$1 Milhão ", font = "Georgia")
        texto_orientador_10 = Label(janela_2, text = "Esse último nível não será possível pedir ajuda;\n\nNão poderá pular a pergunta;\n\nCaso erre a pergunta, receberá R$250.000,00;\n\nCaso acerte ganhará o R$1 Milhao;\n\nEm caso de desistência receberá R$500.000.", font = "Georgia") 
        #Adicionando na tela.
        texto_orientador_1.grid(column = 1, row = 0, padx = 200, pady = 10)
        texto_orientador_2.grid(column = 1, row = 1, padx = 200, pady = 2)
        texto_orientador_3.grid(column = 1, row = 2, padx = 200, pady = 2)
        texto_orientador_4.grid(column = 1, row = 3, padx = 200, pady = 2)
        texto_orientador_5.grid(column = 1, row = 4, padx = 200, pady = 2)
        texto_orientador_6.grid(column = 1, row = 5, padx = 200, pady = 2)
        texto_orientador_7.grid(column = 1, row = 6, padx = 200, pady = 2)
        texto_orientador_8.grid(column = 1, row = 8, padx = 200, pady = 2)
        texto_orientador_9.grid(column = 1, row = 9, padx = 200, pady = 2)
        texto_orientador_10.grid(column = 1, row = 10, padx = 200, pady = 2)
        janela_2.mainloop()
    prints()
    a = input('                         Aperte *Enter* para jogar    ')
    prints()
    nivels(i, j, qtdTrocar, qtdAjuda, perguntas, gabarito, gabaritoRemocao)
    j += 1
    if j == 5:
        j = recursiva(j)
    prints()
    a = input('                     Aperte *Enter* para voltar ao menu ')
    prints()
    
