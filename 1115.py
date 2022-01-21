# -*- coding: utf-8 -*-

while True:
    x, y = input().split()
    x, y = int(x), int(y)

    if x == 0 or y ==0:
        break
    if x>0 and y>0:
        print("primeiro")
    if x>0 and y<0:
        print("quarto")
    if x<0 and y>0:
        print("segundo")
    if x<0 and y<0:
        print("terceiro")
    