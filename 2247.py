# -*- coding: utf-8 -*-

c = 1
while True:
    soma = 0
    n = int(input())
    if n == 0:
        break
    for i in range(0, n):
        j, z = input().split()
        j, z = int(j), int(z)
        soma += j - z
        if i==0:
            print("Teste %d" % (c))
        print(soma)
    print()
    c += 1