a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a<b+c and b<c+a and c<a+b:
    if a==b and b ==c:
        print("Valido-Equilatero")
    elif a == b or b ==c or c ==a:
        print("Valido-Isoceles")
    else: 
        print("Valido-Escaleno")
        
    if(a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")