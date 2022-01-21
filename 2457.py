# -*- coding: utf-8 -*-

c = 0
l = input()
p = input().split()
for i in range(len(p)):
    if l in p[i]:
        c +=1
div = float((c/len(p))*100)
print("%.1f" % div)