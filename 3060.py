# -*- coding: utf-8 -*-

v= int(input())
p= int(input())
#valor de cada parcela
valor=v//p
#achar o resto da divisão
r= v%p
#estrutura de repetição pra informar
for i in range(1,p+1):
    #se o resto for maior ou igual a 1 entra nesse if e repete o "valor+1" pelo mesmo numero do resto
    if i<=r:
        print("%d" % (valor+1))
    else:
        #se o resto for 0 entra aqui
        print("%d" % valor)
        