# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    led = 0
    num = input()
    for j in num:
        if j == '1':
            led += 2
        elif j == '2' or j == '3' or j =='5':
            led +=5
        elif j =='4':
            led +=4
        elif j == '6' or j=='9' or j=='0':
            led += 6
        elif j=='8':
            led+=7
        elif j=='7':
            led+=3
    print("%d leds" % led)