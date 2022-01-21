# -*- coding: utf-8 -*-
menor = 0
posi = 0
n = int(input())
v = input().split()
for j in range(0,n):
    v[j] = int(v[j])

for i in range(0,n):
    if i == 0:
        menor = v[i]
    else:
        if v[i]<menor:
            menor = v[i]
            posi = i
    

print("Menor valor: %d" % (menor))
print("Posicao: %d" % (posi))
    
    