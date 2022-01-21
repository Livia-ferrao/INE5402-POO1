# -*- coding: utf-8 -*-

v = 1
while True:
    n = int(input())
    somaBeto = 0
    somaAldo = 0
    if n ==0:
        break
    for i in range(0, n):
        a, b = input().split()
        a, b = int(a), int(b)
        
        somaBeto +=b
        somaAldo += a

    
    print("Teste %d" % (v))
    if somaBeto > somaAldo:
        print("Beto")
    if somaAldo > somaBeto:
        print("Aldo")
    print()
    v += 1