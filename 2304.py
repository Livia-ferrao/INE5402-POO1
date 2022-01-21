# -*- coding: utf-8 -*-

dinTotal, n = map(int,input().split())
dinD = dinTotal
dinE = dinTotal
dinF = dinTotal

for i in range(n):
    vetor = input().split()
    if vetor[0] == 'A':
        vetor[3] = int(vetor[3])
        if vetor[1]=="D":
            dinD +=vetor[3]
        if vetor[1]=="E":
            dinE +=vetor[3]
        if vetor[1]=="F":
            dinF +=vetor[3]
        if vetor[2]=="D":
            dinD-=vetor[3]
        if vetor[2]=="E":
            dinE-=vetor[3]
        if vetor[2]=="F":
            dinF-=vetor[3]
            
    if vetor[0] == 'C':
        vetor[2] = int(vetor[2])
        if vetor[1] == "D":
            dinD -= vetor[2]
        if vetor[1] == "E":
            dinE -= vetor[2]
        if vetor[1] == "F":
            dinF -= vetor[2]

    if vetor[0] == 'V':
        vetor[2] = int(vetor[2])
        if vetor[1] == "D":
            dinD += vetor[2]
        if vetor[1] == "E":
            dinE += vetor[2]
        if vetor[1] == "F":
            dinF += vetor[2]
    
print(dinD, dinE, dinF)