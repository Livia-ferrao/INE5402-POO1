# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        for i in range(n):
            bin = input()
            dec = int(bin,2)
            char = chr(dec)
            print(char, end='')
        print()

    except EOFError:
        break