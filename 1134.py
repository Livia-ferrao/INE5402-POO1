# -*- coding: utf-8 -*-
comb = 1
alcool = 0
gas = 0
diesel = 0
while comb != 4:
        comb = int(input())
        if comb == 1:
            alcool +=1
        if comb == 2:
            gas +=1
        if comb == 3:
            diesel +=1
  
print('MUITO OBRIGADO')
print('Alcool: %d' % (alcool))
print('Gasolina: %d' % (gas))
print('Diesel: %d' % (diesel))  