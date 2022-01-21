# -*- coding: utf-8 -*-

while True:
    lista = list()
    palitos = 0

    col, lin, minimo = list(map(int, input().split()))

    if col == lin == minimo == 0:
        break

    for processo in range(lin):
        lista.append([int(x) for x in input().split()])

    for coluna in range(len(lista[0])):
        sequencia = 0

        for linha in lista:
            if linha[coluna] == 1:
                sequencia += 1
                if sequencia == minimo:
                    palitos += 1
            else:
                sequencia = 0

    print(palitos)