a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
#definir quantas xicaras Joao possui
x = a//2
#definir quantos ovos Joao possui
y =b//3
#definir quantas colheres de sopa de leite Joao possui
z = c//5
#verificar o menor valores dos 3
d = x
if y< d:
    d = y
if z<d:
    d =z
#printar o menor valor
print(d)
