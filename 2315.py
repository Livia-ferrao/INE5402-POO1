# -*- coding: utf-8 -*-
meses=[0,31,28,31,30,31,30,31,31,30,31,30,31]
dia1,mes1 = input().split()
dia2,mes2 = input().split()
dia1,mes1, dia2,mes2 = int(dia1),int(mes1),int(dia2),int(mes2)
x=0
if mes1 == mes2:
    x += dia2-dia1
else:
    for i in range(mes1,mes2):
        if i == mes1:
            x += meses[i]-dia1
        else:
            x += meses[i]
    x += dia2           

print(x)