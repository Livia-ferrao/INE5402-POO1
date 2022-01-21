# -*- coding: utf-8 -*-

# -- coding: utf-8 --

x,y = input().split()
x = int(x)
y = int(y)

irregulares = []
for i in range(1, x + 1):
    v = input().split()
    irregulares.append(v)

for j in range(1, y + 1):
    irregular = False
    ind_irregular = None
    palavra = input()
    for k in range(0, len(irregulares)):
        if palavra in irregulares[k]:
            irregular = True
            ind_irregular = k
            break

    if irregular:
        print(irregulares[ind_irregular][1])

    elif palavra[len(palavra) - 1] == 'y' and palavra[len(palavra) - 2] not in ['a','e','i','o','u']:
        palavra = list(palavra)
        del palavra[len(palavra) - 1]
        palavra.append('i')
        palavra.append('e')
        palavra.append('s')
        palavra = "".join(palavra)
        print(palavra)

    elif (palavra[len(palavra) - 1] in ['o','s','x']) or (palavra[len(palavra) - 1] == 'h' and palavra[len(palavra) - 2] in ['c','s']):
        print(palavra + 'es')

    else:
        print(palavra + 's')