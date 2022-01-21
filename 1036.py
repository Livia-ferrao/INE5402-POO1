# -*- coding: utf-8 -*-
import math

a,b,c = input().split()
a,b,c = float(a),float(b),float(c)

x=(b**2)-(4*a*c)

if x>0 and a!=0:
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
else:
    print("Impossivel calcular")
    
