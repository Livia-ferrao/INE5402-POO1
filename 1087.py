# -*- coding: utf-8 -*-

while True:
    x1, y1, x2, y2 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if x1 == 0 and x2==0 and y2 ==0 and y2 ==0:
        break
    
    elif x1==x2 and y1==y2:
        print("%d" %0)
    
    elif x1==x2 or y1==y2:
        print("%d" %1)
    
    elif abs(x1-x2) == abs(y1-y2):
        print("%d" %1)
    
    else:
        print("%d" %2)