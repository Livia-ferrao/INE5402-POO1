# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        v = input().split()
        qntd1 = 0
        for i in range(0,n):
            if v[i] == '1':
                qntd1 += 1
        if qntd1 >= n * 2/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break