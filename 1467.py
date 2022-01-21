# -*- coding: utf-8 -*-

while True:
    try:
        a, b, c = input().split()
        a, b, c = int(a), int(b), int(c)

        if a==1 :
            if b ==0:
                if c==0:
                    print("A")
                if c==1: 
                    print("B")
            if b==1:
                if c==0:
                    print("C")
                if c==1: 
                    print("*")
        if a==0:
            if b ==0:
                if c==0:
                    print("*")
                if c==1: 
                    print("C")
            if b==1:
                if c==0:
                    print("B")
                if c==1: 
                    print("A")

    except EOFError:
            break