# -*- coding: utf-8 -*-

n, m= input().split()
n= int(n)
m= int(m)
consegue= "S"
v = input().split()
for i in range (0,len(v)):
    v[i] = int(v[i])
for j in range(1, len(v)):
    if v[j]- v[j-1] > m:
        consegue ='N'
    if j == len(v) - 1:
        if 42195 - v[j] > m:
            consegue= 'N'
print(consegue)