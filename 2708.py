# -*- coding: utf-8 -*-

d = input().split()
turistas = 0
jipes = 0
while d[0] != "ABEND":
    d[1] = int(d[1])
    if d[0] == "SALIDA":
        turistas += d[1]
        jipes +=1
    else:
        turistas -= d[1]
        jipes -= 1
        
    d = input().split()
print(turistas)
print(jipes)