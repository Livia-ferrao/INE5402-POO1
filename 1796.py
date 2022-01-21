# -*- coding: utf-8 -*-

n = int(input())
v = input().split()
for i in range(0,len(v)):
    v[i] = int(v[i])
zero = 0
um = 0
for i in range(0,n):
    if v[i] == 1:
        um += 1
    else:
        zero +=1
if um>=zero:
    print("N")
else:
    print("Y")
    