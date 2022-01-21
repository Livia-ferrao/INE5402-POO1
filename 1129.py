# -*- coding: utf-8 -*-

branco = 0
preto = 0
posi = 0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(0,n):
        v = input().split()
        #passar para int
        for c in range(0,len(v)):
            v[c] = int(v[c])
        #repeticao do vetor
        for j in range(0,len(v)):
            if v[j]<= 127:
                branco += 1
                posi = j
        if branco == 1: 
            if posi == 0:
                print("A")
            if posi == 1:
                print("B")
            if posi == 2:
                print("C")
            if posi == 3:
                print("D")
            if posi == 4:
                print("E")
        else:
            print('*')
        branco = 0
    