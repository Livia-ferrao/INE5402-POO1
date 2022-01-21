# -*- coding: utf-8 -*-

s = input()
qntd1 = 0
for i in range(0,len(s)):
    if s[i] == '1':
        qntd1 +=1
if qntd1 % 2 == 0:
    print(s + '0')
else:
    print(s + '1')