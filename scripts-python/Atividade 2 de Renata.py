# z= medico  y = dia  w = hora
# O Segredo esta nessa matriz 
matriz = [[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],],
          [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]]
          
def Menu(x):
    print()
    print('     Clínica Dra Ivone')
    print()
    print('  MENU')
    print()
    print('[1]- Escolha médico para ver horários disponíveis')
    print('[2]- Escolha especialidade para ver horários disponíveis')
    print('[3]- Escolha dia da semana e especialidade para saber horários disponíveis')
    print('[4]- Agendar horário')
    print('[0]- Sair')
    print()

def num1(x):
    print(' Oftamologistas       Cardiologistas          Pediatras') 
    print('Dr.Mauro --->(1)    Dra.Rita   --->(4)    Dra.Alice  --->(7)')
    print('Dr.Lucas --->(2)    Dr.Cláudio --->(5)    Dr.Ruan    --->(8)')
    print('Dra.Ana  --->(3)    Dra.Carla  --->(6)    Dr.Antônio --->(9)')
    print('                                          Dra.Elis   --->(0)')
    print()

def num2(x):
    print('(1)Oftalmologista   (2) Cardiologista   (3) Pediatra')
    print()
    
def num3(x): 
    print('(1)Segunda  (2)Terça  (3)Quarta  (4)Quinta  (5)Sexta')
    print()
    print('(1)Oftalmologista   (2) Cardiologista   (3) Pediatra')
    print()

def fun1(z):
    if z == 1:        
        print('Dr. Mauro - Oftalmologista ')
        print('Segunda - Manhã, Tarde e Noite')
        print('Quarta - Manhã e Tarde')
        print('Sexta - Manhã e Noite')
    elif z == 2:
        print('Dr. Lucas - Oftalmologista ')
        print('Terça - Manhã e Tarde')
        print('Quinta - Manhã, Tarde e Noite')
        print('Sexta - Tarde e Noite ')
    elif z == 3:
        print('Dra. Ana - Oftalmologista ')
        print('Segunda - Manhã e Tarde')
        print('Terça - Manhã e Tarde')
        print('Quarta - Manhã e Tarde')
        print('Quinta - Manhã e Tarde')
        print('Sexta - Manhã e Tarde')
    elif z == 4:
        print('Dra. Rita - Cardiologista')
        print('Quarta - Tarde e Noite')
        print('Quinta - Manhã, Tarde e Noite')
        print('Sexta - Tarde e Noite')
    elif z == 5:
        print('Dr.Cláudio - Cardiologista')
        print('Segunda - Manhã e Noite')
        print('Terça - Tarde e Noite')
        print('Quarta - Manhã e Tarde')
    elif z == 6:
        print('Dra.Carla - Cardiologista')
        print('Segunda - Manhã, Tarde e Noite')
        print('Terça - Manhã, Tarde e Noite')
    elif z == 7:
        print('Dra.Alice - Pediatra')
        print('Segunda - Tarde e Noite')
        print('Quarta - Tarde e Noite')
        print('Sexta - Tarde e Noite')
    elif z == 8:
        print('Dr.Ruan - Pediatra')
        print('Terça - Manhã e Tarde')
        print('Qunta - Manhã e Tarde')
        print('Sexta - Manhã e Tarde')
    elif z == 9:
        print('Dr.Antônio - Pediatra')
        print('Segunda - Manhã e Tarde')
        print('Terça - Manhã e Tarde')
        print('Quarta - Manhã e Tarde')
    elif z == 0:
        print('Dra.Elis - Pediatra')
        print('Segunda - Manhã, Tarde e Noite')
        print('Sexta - Manhã, Tarde e Noite')

def fun2(z):
    if (z == 1):
        print('Segunda-------------------------')
        print('Dr. Mauro - Manhã, Tarde e Noite')
        print('Dra. Ana  - Manhã e Tarde')
        print('Terça --------------------------')
        print('Dr. Lucas - Manhã e Tarde')
        print('Dra. Ana  - Manhã e Tarde')
        print('Quarta -------------------------')
        print('Dr. Mauro - Manhã e Tarde')
        print('Dra. Ana  - Manhã e Tarde')
        print('Quinta -------------------------')
        print('Dr. Lucas - Manhã, Tarde e Noite')
        print('Dra. Ana  - Manhã e Tarde')
        print('Sexta --------------------------')
        print('Dr. Mauro - Manhã e Noite')
        print('Dr. Lucas - Tarde e Noite ')
        print('Dra. Ana  - Manhã e Tarde')
    elif (z == 2):
        print('Segunda-------------------------')
        print('Dr. Cláudio - Manhã e Noite')
        print('Dra. Carla  - Manhã, Tarde e Noite')
        print('Terça --------------------------')
        print('Dr. Cláudio - Tarde e Noite')
        print('Dra. Carla  - Manhã, Tarde e Noite')
        print('Quarta -------------------------')
        print('Dra. Rita   - Tarde e Noite')
        print('Dr. Cláudio - Manhã e Tarde')
        print('Quinta -------------------------')
        print('Dra. Rita - Manhã, Tarde e Noite')
        print('Sexta --------------------------')
        print('Dra. Rita - Tarde e Noite')
    elif (z == 3):
        print('Segunda-------------------------')
        print('Dra. Alice  - Tarde e Noite')
        print('Dr. Antônio - Manhã e Tarde')
        print('Dra. Elis   - Manhã, Tarde e Noite')
        print('Terça --------------------------')
        print('Dr. Ruan    - Manhã e Tarde')
        print('Dr. Antônio - Manhã e Tarde')
        print('Quarta -------------------------')
        print('Dra. Alice  - Tarde e Noite')
        print('Dr. Antônio - Manhã e Tarde')
        print('Quinta -------------------------')
        print('Dr. Ruan - Manhã e Tarde')
        print('Sexta --------------------------')
        print('Dra. Alice - Tarde e Noite')
        print('Dr. Ruan   - Manhã e Tarde')
        print('Dra. Elis  - Manhã, Tarde e Noite')

def fun3(y,z):
    if (z == 1):
        if(y == 1):
            print('Dr. Mauro - Manhã, Tarde e Noite')
            print('Dra. Ana  - Manhã e Tarde')
        elif(y == 2):
            print('Dr. Lucas - Manhã e Tarde')
            print('Dra. Ana  - Manhã e Tarde')
        elif(y == 3):
            print('Dr. Mauro - Manhã e Tarde')
            print('Dra. Ana  - Manhã e Tarde')
        elif(y == 4):
            print('Dr. Lucas - Manhã, Tarde e Noite')
            print('Dra. Ana  - Manhã e Tarde')
        elif(y == 5):
            print('Dr. Mauro - Manhã e Noite')
            print('Dr. Lucas - Tarde e Noite ')
            print('Dra. Ana  - Manhã e Tarde')
    elif (z == 2):
        if(y == 1):
            print('Dr. Cláudio - Manhã e Noite')
            print('Dra. Carla  - Manhã, Tarde e Noite')
        elif(y == 2):
            print('Dr. Cláudio - Tarde e Noite')
            print('Dra. Carla  - Manhã, Tarde e Noite')
        elif(y == 3):
            print('Dra. Rita   - Tarde e Noite')
            print('Dr. Cláudio - Manhã e Tarde')
        elif(y == 4):
            print('Dra. Rita - Manhã, Tarde e Noite')
        elif(y == 5):
            print('Dra. Rita - Tarde e Noite')
    elif (z == 3):
        if(y == 1):
            print('Dra. Alice  - Tarde e Noite')
            print('Dr. Antônio - Manhã e Tarde')
            print('Dra. Elis   - Manhã, Tarde e Noite')
        elif(y == 2):
            print('Dr. Ruan    - Manhã e Tarde')
            print('Dr. Antônio - Manhã e Tarde')
        elif(y == 3):
            print('Dra. Alice  - Tarde e Noite')
            print('Dr. Antônio - Manhã e Tarde')
        elif(y == 4):
            print('Dr. Ruan - Manhã e Tarde')
        elif(y == 5):
            print('Dra. Alice - Tarde e Noite')
            print('Dr. Ruan   - Manhã e Tarde')
            print('Dra. Elis  - Manhã, Tarde e Noite')

def fun4(z):
    if z == 1:        
        print('Dr. Mauro - Oftalmologista ')
        print('(1) - Segunda - Manhã, Tarde e Noite')
        print('(2) - Quarta - Manhã e Tarde')
        print('(3) - Sexta - Manhã e Noite')
    elif z == 2:
        print('Dr. Lucas - Oftalmologista ')
        print('(1) - Terça - Manhã e Tarde')
        print('(2) - Quinta - Manhã, Tarde e Noite')
        print('(3) - Sexta - Tarde e Noite ')
    elif z == 3:
        print('Dra. Ana - Oftalmologista ')
        print('(1) - Segunda - Manhã e Tarde')
        print('(2) - Terça - Manhã e Tarde')
        print('(3) - Quarta - Manhã e Tarde')
        print('(4) - Quinta - Manhã e Tarde')
        print('(5) - Sexta - Manhã e Tarde')
    elif z == 4:
        print('Dra. Rita - Cardiologista')
        print('(1) - Quarta - Tarde e Noite')
        print('(2) - Quinta - Manhã, Tarde e Noite')
        print('(3) - Sexta - Tarde e Noite')
    elif z == 5:
        print('Dr.Cláudio - Cardiologista')
        print('(1) - Segunda - Manhã e Noite')
        print('(2) - Terça - Tarde e Noite')
        print('(3) - Quarta - Manhã e Tarde')
    elif z == 6:
        print('Dra.Carla - Cardiologista')
        print('(1) - Segunda - Manhã, Tarde e Noite')
        print('(2) - Terça - Manhã, Tarde e Noite')
    elif z == 7:
        print('Dra.Alice - Pediatra')
        print('(1) - Segunda - Tarde e Noite')
        print('(2) - Quarta - Tarde e Noite')
        print('(3) - Sexta - Tarde e Noite')
    elif z == 8:
        print('Dr.Ruan - Pediatra')
        print('(1) - Terça - Manhã e Tarde')
        print('(2) - Qunta - Manhã e Tarde')
        print('(3) - Sexta - Manhã e Tarde')
    elif z == 9:
        print('Dr.Antônio - Pediatra')
        print('(1) - Segunda - Manhã e Tarde')
        print('(2) - Terça - Manhã e Tarde')
        print('(3) - Quarta - Manhã e Tarde')
    elif z == 0:
        print('Dra.Elis - Pediatra')
        print('(1) - Segunda - Manhã, Tarde e Noite')
        print('(2) - Sexta - Manhã, Tarde e Noite')

def fun5(z,y):
    if z == 1:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 3:
            print('(3) - Sexta - Manhã e Noite')
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
    elif z == 2:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 3:
            print('14h -->(0)   15h --->(1)   16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
    elif z == 3:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 3:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 4:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 5:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
    elif z == 4:
        if y == 1:
            print('14h -->(0)   15h --->(1)  16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 3:
            print('14h -->(0)   15h --->(1)  16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
    elif z == 5:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
        elif y == 2:
            print('14h -->(0)   15h --->(1)   16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
        elif y == 3:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)   16h -->(6)   17h -->(7)')
    elif z == 6:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
    elif z == 7:
        if y == 1:
            print('14h -->(0)   15h --->(1)   16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
        elif y == 2:
            print('14h -->(0)   15h --->(1)   16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
        elif y == 3:
            print('14h -->(0)   15h --->(1)   16h -->(2)   17h -->(3)   18h -->(4)   19h -->(5)   20h -->(6)')
    elif z == 8:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 3:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
    elif z == 9:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
        elif y == 3:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)')
    elif z == 0:
        if y == 1:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')
        elif y == 2:
            print('8h -->(0)   9h -->(1)   10h -->(2)   11h -->(3)   14h -->(4)   15h --->(5)')
            print('16h -->(6)   17h -->(7)   18h -->(8)   19h -->(9)   20h -->(10)')


#MENU
            
x = 1
while x != 0 :
    Menu(x)
    x = int(input('Digite o número da opção que deseja execultar: '))
    print()
    if x == 1:
        num1(x)
        z = int(input('Digite o número do médico para ver os horarios: '))
        print()
        fun1(z)
        print()
    elif x == 2:
        num2(x)
        z = int(input('Digite o número da especialidade escolhida: '))
        print()
        fun2(z)
        print()
    elif x == 3:
        num3(x)
        y = int(input('Digite o número do dia em que deseja ser atendido: '))
        z = int(input('Digite o número da especialidade escolhida: '))
        print()
        fun3(y,z)
        print()
    elif x == 4:
        num1(x)
        z = int(input('Digite o número do médico para poder agendar um horario: '))
        print()
        fun4(z)
        print()
        y = int(input('Digite o número do dia para poder agendar um horario: '))
        fun5(z,y)
        print()
        w = int(input('Digite o número corespondente ao horario escolhido para poder agendar um horario: '))
        print()
        num = 0
        nu = 1
        if(matriz[z][y][w]) != 1:
            print('Horario indisponivel! Escolha outro Horario!')
        if (matriz[z][y][w]) == 1:
            print('Horario disponivel!')
            print()
            k = int(input('Deseja ajendar nesse horario? (0)--> Sim   (1)--> Não  : '))
            if k == 0:
                print('Horario Agendado!')
                matrizfi = []
                for a in range(12):
                    matr = []
                    for b in range(6):
                        lista = []
                        for c in range(15):
                            if (a == z) and (b == y) and (c == w):
                                lista.append(num)
                            elif(matriz[a][b][c] == 0):
                                lista.append(num)
                            else:
                                lista.append(nu)
                        matr.append(lista)
                    matrizfi.append(matr)
                matriz = matrizfi
            

    print('')
    a = input('') 



#ATENÇÕON EM CASO DE DUVIDAS NO CODIGO FOINT ENTRAR EM CONTACTO COM BY: GEROGE AZEVEDO DE OLIVEIRA.
