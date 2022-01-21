# -*- coding: utf-8 -*-
l, a, p, r = input().split()
l = int(l)
a = int(a)
p = int(p)
r = int(r)

diametro = r + r;

diagonal = ((l*l) + (a * a) + (p * p))**(1/2);

if (diagonal <= diametro):
    print('S')
else:
    print('N')
