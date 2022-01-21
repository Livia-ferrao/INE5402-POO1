n = int(input())
a = n
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n05 = 0
n02 = 0
n01 = 0

if n>=100:
    n100 = n//100
    n = n%100
if n>=50:
    n50 = n//50
    n = n%50
if n>=20:
    n20 = n//20
    n = n%20
if n>=10:
    n10 = n//10
    n = n%10
if n>=5:
    n05 = n//5
    n = n%5
if n>=2:
    n02 = n//2
    n = n%2
if n>=1:
    n01 = n//1
    n = n%1
    
print(a)
print("%d nota(s) de R$ 100,00" % n100)
print("%d nota(s) de R$ 50,00" % n50)
print("%d nota(s) de R$ 20,00" % n20)
print("%d nota(s) de R$ 10,00" % n10)
print("%d nota(s) de R$ 5,00" % n05)
print("%d nota(s) de R$ 2,00" % n02)
print("%d nota(s) de R$ 1,00" % n01)