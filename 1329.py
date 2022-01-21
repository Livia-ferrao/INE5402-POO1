# -*- coding: utf-8 -*-

mary = 0
john = 0
while True:
    n = int(input())
    if n == 0:
        break
    v = input().split()
    for j in range(0,len(v)):
        v[j] = int(v[j])
    for i in range(0,len(v)):
        if v[i] == 0:
            mary += 1
        else:
            john +=1
    print("Mary won %d times and John won %d times" % (mary,john))
    mary = 0
    john = 0
    