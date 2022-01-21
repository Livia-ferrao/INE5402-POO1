# -*- coding: utf-8 -*-

v = int(input())

lista_zeros = [0]*v

for i in range(v):
    bomba = int(input())
    if bomba == 1 and (i) > 0:
        lista_zeros[i-1] += 1
    if bomba == 1:
        lista_zeros[i] += 1
    if bomba == 1 and (i+1) < v:
        lista_zeros[i+1] += 1

for i in lista_zeros:
    print (i)