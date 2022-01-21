# -*- coding: utf-8 -*-

while True:
    try:
        lista = []

        f, v = input().split()
        f, v = int(f),int(v)
        l = input().split()

        for i in range(0,len(l)):
            l[i] = int(l[i])
        l.sort()

        for i in range(1,f+1):
            if i not in l:
                lista.append(i)
                
        if v == f:
            print("*")
        else:
            for i in range(0,len(lista)):
                print(lista[i], end= " ")
            print("")
        
                
    except EOFError:
        break