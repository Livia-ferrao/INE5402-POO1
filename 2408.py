# -*- coding: utf-8 -*-

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>c and b>a:
    if a>c:
        print(a)
    else: 
        print(c)
else:
    if b>a:
        print(b)
    else:
        print(a)
