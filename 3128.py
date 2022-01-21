# -*- coding: utf-8 -*-

#ler as duas idades
i1 = int(input())
i2 = int(input())

#verificar se as idades são maiores que 6
if (i1>=6 and i2>=6):
    #verificar se as idade de um deles é maior que 18 ou as duas são maiores que 14
    if(i1>=18 or i2>=18) or (i1>=14 and i2>=14):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
  