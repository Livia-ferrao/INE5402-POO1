# -*- coding: utf-8 -*-

i, f = input().split()
i, f = int(i), int(f)

if i ==f:
    t = 24
if i>f:
    t1 = 24 - i
    t2 = f
    t = t1+t2
if f>i:
    t = f - i
    
print("O JOGO DUROU %d HORA(S)" % (t))