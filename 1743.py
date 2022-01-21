# -*- coding: utf-8 -*-

v = input().split()
for i in range (0,len(v)):
    v[i] = int(v[i])
a = input().split()
for i in range (0,len(v)):
    a[i] = int(a[i])
    
for i in range(0,len(v)):
    if v[i] == a[i]:
        s = 0
        break
    else:
        s = 1
if s == 0:
    print("N")
else:
    print("Y")
    
    