N1, D1, V1 = input().split()
N1, D1, V1 = int(N1), int(D1), int(V1)

N2, D2, V2 = input().split()
N2, D2, V2 = int(N2), int(D2), int(V2)

x = (D1/1000)/V1
y = (D2/1000)/V2

if x<y:
    print(N1)
else:
    print(N2)