# -*- coding: utf-8 -*-

posi = 0
dist = 0
menorDist = 0
#ler o primeiro valor para saber quantas repetições serão
n = int(input())
for i in range(1,n+1):
    #ler o número de bolas além da branca
    b = int(input())
    #ler a coordenada da bola branca
    x, y = input().split()
    x, y = int(x), int(y)
    # repetir a quantidade de bolas
    for j in range(1,b+1):
        #ler a coordenada da primeira bola(sem ser a branca)
        x1, y2 = input().split()
        x1, y2 = int(x1), int(y2)
        # definir a distancia da bola branca com a bola lida em cima
        dist = (((x1-x)**2) + ((y2-y)**2))**(1/2)
        # denifir qual a menor distancia e assim atribuir a posição(j) da bola
        # no inicio a menor distancia será da primeira bola lida
        if j == 1:
            menorDist = dist
            posi = j
        else:
            if dist<menorDist:
                menorDist = dist
                posi = j
    print(posi)