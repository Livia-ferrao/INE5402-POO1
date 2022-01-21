# -*- coding: utf-8 -*-

o, b, i = input().split()
o, b, i = float(o), float(b), float(i)

if o == b or b == i or i == o:
    print("Empate")
if o<b and o <i:
    print("Otavio")
if b<o and b<i:
    print("Bruno")
if i<o and i< b:
    print("Ian")