# -*- coding: utf-8 -*-

l = int(input())
qnt = 1
while True:
    if(l<2):
        break
    l = l/2
    qnt = qnt*4
print(qnt)