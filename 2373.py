# -*- coding: utf-8 -*-

n = int(input())
soma = 0
for i in range(0, n):
    c, l = input().split()
    c, l = int(c), int(l)
    if c>l:
        soma += l
print(soma)