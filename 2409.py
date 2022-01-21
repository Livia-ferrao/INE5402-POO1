a, b, c = input().split()
a, b, c = int(a),int(b),int(c)

h, l = input().split()
h, l =int(h), int(l)

if a<=h and b<=l:
    print('S')
elif a<=h and c<=l:
    print('S')
elif b<=h and a<=l:
    print('S')
elif b<=h and c<=l:
    print('S')
elif c<=h and a<=l:
    print('S')
elif c<=h and b<=l:
    print('S')
else:
    print('N')
