# -*- coding: utf-8 -*-

lista = []
total = 0
v = 0
t = int(input())
for numero in range(t):
    x = int(input())
    lista.append(x)
lista.sort(reverse=True)
for num in range(t-1):
    if(lista[num] - lista[num+1]) <=10:
        total+= lista[num] - lista[num+1]
    else:
        v +=1
print((total+10)+(v*10))