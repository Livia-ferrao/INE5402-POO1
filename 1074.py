# -*- coding: utf-8 -*-

n = int(input())
i = 0
while i < n:
    num = int(input())
    if num%2==0 and num>0:
        print("EVEN POSITIVE")
    if num%2==0 and num<0:
        print("EVEN NEGATIVE")
    if num%2==1 and num>0:
        print("ODD POSITIVE")
    if num%2==1 and num<0:
        print("ODD NEGATIVE")
    if num == 0:
        print("NULL")
    i +=1