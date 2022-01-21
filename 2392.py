# -*- coding: utf-8 -*-

numPedra,numSapo= input().split()
numPedra,numSapo = int(numPedra),int(numSapo)
lista = []
for i in range(0,numSapo):
    posi,pulo = input().split()
    posi,pulo = int(posi),int(pulo)
    for j in range(posi,0,-pulo):
        lista.append(j)
    for k in range(posi,numPedra+1,pulo):
        lista.append(k)
for l in range(1,numPedra+1):
    if l in lista:
        print('1')
    else:
        print('0')
