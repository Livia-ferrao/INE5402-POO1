# -*- coding: utf-8 -*-
n = int(input())
for i in range(0, n):
    k = int(input())
    for i in range(0, k):
        cat = int(input())
        if cat == 1:
            print("Rolien")
        elif cat == 2:
            print("Naej")
        elif cat == 3:
            print("Elehcim")
        else:
            print("Odranoel")