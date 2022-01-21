# -*- coding: utf-8 -*-
capMax = 0
a = 0
num, cap = input().split()
num, cap = int(num), int(cap)
for i in range(0, num):
    saiu, entrou = input().split()
    saiu, entrou = int(saiu), int(entrou)
    
    capMax += entrou - saiu
    
    if capMax > cap:
        a = 1
        print("S")
        break
if a != 1:
    print("N")