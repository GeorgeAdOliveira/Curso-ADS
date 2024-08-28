print()
print('Clínica Médica  Dra. Ivone')
print()
print('(1) Oftalmologista')   
print('(2) Cardiologista')
print('(3) Pediatra')
print()
print('(1)Segunda (2)Terça (3)Quarta (4)Quinta (5)Sexta')
print()
x = int(input('Digite o número da especialidade escolhida: '))
print()
y = int(input('Digite o número do dia em que deseja ser atendido: '))
print()
if (x == 1):
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
elif (x == 2):
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
elif (x == 3):
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
