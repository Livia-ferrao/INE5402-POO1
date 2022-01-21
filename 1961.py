# -*- coding: utf-8 -*-

h,c = input().split()
h,c = int(h),int(c)

v = input().split()
for i in range(0,len(v)):
    v[i] = int(v[i])

for i in range(1,len(v)):
    if abs(v[i] - v[i-1]) <= h:
        s = 1
    else:
        s = 0
        break
if s ==1:
    print("YOU WIN")
else:
    print("GAME OVER")
    