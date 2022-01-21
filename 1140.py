# -*- coding: utf-8 -*-

while True:
    tautograma = True
    t = input()
    
    if t == '*':
        break
    t = t.split()
    letra = t[0][0]
    
    for palavra in t:
        if palavra[0].lower() != letra.lower():
            tautograma = False
            break

    if tautograma:
        print("Y")
    else:
        print("N")
