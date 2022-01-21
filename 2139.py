# -*- coding: utf-8 -*-

l = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    try:  
        mes, dia = input().split()
        mes, dia = int(mes), int(dia)
        
        if mes == 12 and dia ==24:
            print("E vespera de natal!")
            
        elif mes == 12 and dia ==25:
            print("E natal!")
        elif mes==12 and dia>25:
            print("Ja passou!")
        else:
            x = l[mes-1] - dia
            for i in range(mes, len(l)):
                x+= l[i]    
            x -= 6  
            print("Faltam %d dias para o natal!" % x);
            x = 0
    except EOFError:
        break