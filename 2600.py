# -*- coding: utf-8 -*-
caso = int(input())
for i in range(0, caso):
    a1 = int(input())
    a2, a3, a4, a5 = map(int,input().split())
    a6 = int(input())
    if(a1 and a2 and a3 and a4 and a5 and a6)<7 and (a1 and a2 and a3 and a4 and a5 and a6)>0 and (a1!=a2!=a3!=a4!=a5!=a6) :
        if (a1+a6) == 7 and (a2+a4)==7 and (a3+a5)==7:
            print("SIM")
        else:
            print("NAO")
    else:
        print("NAO")