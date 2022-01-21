# -*- coding: utf-8 -*-

while True:
    str = ""
    num, valor = input().split()
    if num == '0'and valor == '0':
        break
    for n in valor:
        if n != num:
            str += n

    if str.count("0") == len(str):
            str = "0"
    
    print(int(str))