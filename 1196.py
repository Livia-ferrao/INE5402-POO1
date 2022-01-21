# -*- coding: utf-8 -*-

lista =  '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
while True:
    try:
        letra = ''
        str = input()
        for i in str:
            if i == ' ':
                letra += i
            else:
                index = lista.index(i)
                letra += lista[index-1]
        print(letra)
    except EOFError:
        break