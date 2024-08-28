n = int(input())
x = []
i = 0
num = 1
for i in range(n):
    l = input()
    if (l == 'F E C A'):
        x.append(num)
    if (l == 'A C E F'):
        x.append(num)
    if (l == 'E C A F'):
        x.append(num)
for i in x :
    i += 1
print(i)
