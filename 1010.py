# -*- coding: utf-8 -*-

cod1, num1, v1 = input().split()
cod1, num1, v1 = int(cod1),int(num1),float(v1)
cod2, num2, v2 = input().split()
cod2, num2, v2 = int(cod2),int(num2),float(v2)

r1 = v1*num1
r2 = v2*num2
soma = r1+r2

print("VALOR A PAGAR: R$ %.2f"% (soma)) 
