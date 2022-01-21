# -*- coding: utf-8 -*-

#ler idade de Mônica
m = int(input())
#ler idade dos filhos
i1 = int(input())
i2 = int(input())

#descobrir idade do outro filho
i3 = m - i1 - i2

#descobrir quem tem mais idade e printar o maior
if i2>i1 and i2>i3:
    print(i2)
elif i3>i1 and i3>i2:
    print(i3)
elif i1>i2 and i1>i3:
    print(i1)
