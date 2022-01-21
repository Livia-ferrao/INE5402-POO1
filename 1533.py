# -*- coding: utf-8 -*-

while True:
    a= int(input())
    if a == 0:
        break
    c = list(map(int,input().split()))
    s=c.copy()
    s.sort(reverse=True)
    print(c.index(s[1]) + 1)
