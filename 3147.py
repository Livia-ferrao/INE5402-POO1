# -*- coding: utf-8 -*-

#ler as quantidades em cada exército
h, e, a, o, w, x = input().split()
h, e, a, o, w, x = int(h),int(e),int(a),int(o),int(w),int(x)

#somar os exercitos do bem
bem = h+e+a
#somar os exercitos do mau
mau = o+w

#se o bem perder para o mau juntar exercito com águias
if bem<=mau:
    #adicionar águias
    bem += x
    #bem ainda menor que o mau ele perde
    if bem<mau:
        print("Sauron has returned.")
    #bem maior que o mau ele ganha
    if bem>=mau:
        print("Middle-earth is safe.")
#bem vença mal diretamente
else:
    print("Middle-earth is safe.")