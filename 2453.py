# -*- coding: utf-8 -*-

msg = ''
p = input().split()
for i in range(len(p)):
    for j in range(1,len(p[i]),2):
        msg += p[i][j]
    msg += ' '
print(msg[0:-1])