# -*- coding: utf-8 -*-
a = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:', end='\n')
for c in range(0, len(cedulas)):
    b = a // cedulas[c]
    print(f'{b:.0f} nota(s) de R$ {cedulas[c]}.00', end='\n')
    a = a - b * cedulas[c]
print('MOEDAS:', end='\n')
for c in range(0, len(moedas)-1):
    b = a // moedas[c]
    a -= b*moedas[c]
    print(f'{b:.0f} moeda(s) de R$ {moedas[c]:.2f}', end='\n')
print(f'{(a*100):.0f} moeda(s) de R$ {moedas[-1]:.2f}', end='\n')