# -*- coding: utf-8 -*-
n = 1
soma = 0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1, n+1):
        soma += i*i
    print(soma)
    soma = 0