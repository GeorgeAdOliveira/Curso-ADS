n = int(input(''))
a = n//100
b = (n%100)//50
c = ((n%100)%50)//20
d = (((n%100)%50)%20)//10
e = ((((n%100)%50)%20)%10)//5
f = (((((n%100)%50)%20)%10)%5)//2
h = (((((n%100)%50)%20)%10)%5)%2//1
print(n)
print('%d nota(s) de R$ 100,00'%a)
print('%d nota(s) de R$ 50,00'%b)
print('%d nota(s) de R$ 20,00'%c)
print('%d nota(s) de R$ 10,00'%d)
print('%d nota(s) de R$ 5,00'%e)
print('%d nota(s) de R$ 2,00'%f)
print('%d moeda(s) de R$ 1,00'%h)
