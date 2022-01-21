# -*- coding: utf-8 -*-

n = int(input())
c =0
soma = 0
while c<n:
    x, y = input().split()
    x, y = int(x), int(y)
    if x<y:
        for i in range (x+1, y):
            if i%2==1:
                soma += i
        print(soma)
        soma = 0
    elif y<x:
        for i in range (y+1, x):
            if i%2==1:
                soma += i
        print(soma)
        soma = 0
    else:
        print("%d" % 0)
    c +=1