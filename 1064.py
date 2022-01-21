# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
s=0
m =0
t =[a,b,c,d,e,f]
for n in t:
  if n > 0:
    s += 1
    m += n
print('%d valores positivos' % s)
print('%.1f' % (m/s))