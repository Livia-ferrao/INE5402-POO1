# -*- coding: utf-8 -*-

c = 1
while True:
    n = int(input())
    quadradinhos = (2**n + 1)**2
    if 0 <= n <= 15:
        print("Teste %d" % c)
        print(quadradinhos)
        print('')
        c += 1
    elif n == -1:
        break