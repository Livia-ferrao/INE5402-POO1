# -*- coding: utf-8 -*-

saldos, cont = input().split()
saldos, cont = int(saldos), int(cont)
menor = 0

for i in range (0,saldos):
    dep = int(input())
    if dep<0:
        cont += dep
    else: 
        cont += dep
    if i==0:
        menor = cont
    if cont<menor:
        menor = cont
        
print(menor)