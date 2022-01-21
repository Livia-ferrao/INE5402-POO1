# -*- coding: utf-8 -*-

i = 1
while True:
    
    nota50 = 0
    nota10 = 0
    nota05 = 0
    nota01 = 0
    v = int(input())
    if v == 0:
        break
    if v>=50:
        nota50 = v//50
        v = v%50
    if v>=10:
        nota10 = v//10
        v = v%10
    if v>=5:
        nota05 += v//5
        v = v%5
    if v>=1:
        nota01 = v//1
        v = v%1
        
    print("Teste %d" % (i))
    print(nota50, nota10, nota05, nota01)
    print()
    i += 1