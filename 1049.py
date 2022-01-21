palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            print("aguia")
        if palavra3 == 'onivoro':
            print("pomba")
    if palavra2 == 'mamifero':
        if palavra3 == 'onivoro':
            print("homem")
        if palavra3 == 'herbivoro':
            print("vaca")
if palavra1 == 'invertebrado':
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            print('pulga')
        if palavra3 == 'herbivoro':
            print('lagarta')
    if palavra2 == 'anelideo':
        if palavra3 == 'hematofago':
            print('sanguessuga')
        if palavra3 == 'onivoro':
            print('minhoca') 
