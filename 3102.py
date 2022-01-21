# -*- coding: utf-8 -*-

import math
t = int(input())
for numero in range(t):
    x1,y1,x2,y2,x3,y3 = map(int, input().split())
    d12 = math.sqrt(((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
    d23 = math.sqrt(((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2)))
    d31 = math.sqrt(((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)))
    p = (d12+d23+d31)/2
    A = math.sqrt(p*(p-d12)*(p-d23)*(p-d31))
    print("{:.3f}".format(A))