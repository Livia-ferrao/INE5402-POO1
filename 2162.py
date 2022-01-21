# -*- coding: utf-8 -*-

n = int(input())
hs = input().split()
for i in range(0,n):
    hs[i] = int(hs[i])
    
padrao = 1
#procura vale seguido de vale (idem pico)
forma = 0 #1 vale, 2 pico

for i in range(1,n):
    if hs[i] < hs[i-1]:
        if forma == 1: #se vale
            padrao = 0
            break
        else:
            forma =1
    elif hs[i] > hs[i-1]:
        if forma == 2: #se pico
            padrao = 0
            break
        else:
            forma = 2
    else:
        padrao = 0
        break
    
print(padrao)