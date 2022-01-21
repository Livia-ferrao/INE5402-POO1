# -*- coding: utf-8 -*-
while True:
    try:
        h, m = input().split()
        h, m = int(h), int(m)

        horas = int(h/30)
        minutos = int(m/6)

        print("%.2d:%.2d" % (horas,minutos))
    except EOFError:
        break