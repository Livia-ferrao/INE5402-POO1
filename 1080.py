# -*- coding: utf-8 -*-

for i in range(1,101):
    num = int(input())
    if i ==1:
        maiorValor= num
        posi = i
    if num> maiorValor:
        maiorValor = num
        posi = i
print(maiorValor)
print(posi)