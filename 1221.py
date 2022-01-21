# -*- coding: utf-8 -*-

n = int(input())
x = 0
primo = 0

while x < n:
    num = int(input())
    if num ==2:
        primo = 0
    else: 
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                primo = 1
            
    if primo == 1 or num ==1:
        print("Not Prime")
    elif primo == 0:
        print("Prime")
        
    primo = 0
    x += 1