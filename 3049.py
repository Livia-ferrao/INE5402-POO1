# -*- coding: utf-8 -*-

#ler valores T e B
b = int(input())
t = int(input())
#bases do trapézio
b1=160-t
t1=160-b
#calcular área dos dois lados
areaFelix=((b+t)*70)/2
areaMarzia=((b1+t1)*70)/2

#verificar qual a maior área e imprimir quem ficou com a nota de 100
if areaMarzia < areaFelix:
    print("1")
elif areaMarzia > areaFelix:
    print("2")
# mesma área ninguém fica com a nota
elif areaMarzia == areaFelix:
    print("0")