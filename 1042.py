a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if a>b and a>c:
    if b>c:
        print(c)
        print(b)
        print(a)
    if c>b:
        print(b)
        print(c)
        print(a)
elif b>a and b>c:
    if a>c:
        print(c)
        print(a)
        print(b)
    if c>a:
        print(a)
        print(c)
        print(b)
elif c>a and c>b:
    if a>b:
        print(b)
        print(a)
        print(c)
    if b>a:
        print(a)
        print(b)
        print(c)
        
print()
print(a)
print(b)
print(c)