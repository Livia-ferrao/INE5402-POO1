a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a<b+c and c<b+a and b<a+c:
    perimetro = a+b+c
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((a+b)*c)/2
    print("Area = %.1f" % area)