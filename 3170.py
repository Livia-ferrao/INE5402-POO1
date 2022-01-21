while True:
    try:
        hora, minuto = input().split(':')
        hora = int(hora)
        minuto = int(minuto)

        vetor_hora = [' ',' ',' ',' ']  #Respectivamente representa 8,4,2 e 1
        vetor_minuto = [' ',' ',' ',' ',' ',' '] #Respectivamente representa 32,16,8,4,2 e 1
        resto = int

        if hora >= 8:
            resto = hora % 8
            vetor_hora[0] = 'o'
        else:
            resto = hora

        if resto >= 4:        #A partir de agora se trabalha com o resto
            resto = hora % 4
            vetor_hora[1] = 'o'
        if resto >= 2:
            resto = hora % 2
            vetor_hora[2] = 'o'
        if resto == 1:
            vetor_hora[3] = 'o'

        resto = 0
        if minuto >= 32:
            resto = minuto % 32
            vetor_minuto[0] = 'o'
        else:
            resto = minuto

        if resto >= 16:
            resto = minuto % 16
            vetor_minuto[1] = 'o'
        if resto >= 8:
            resto = minuto % 8
            vetor_minuto[2] = 'o'
        if resto >= 4:
            resto = minuto % 4
            vetor_minuto[3] = 'o'
        if resto >= 2:
            resto = minuto % 2
            vetor_minuto[4] = 'o'
        if resto == 1:
            vetor_minuto[5] = 'o'

        print(' ________________')
        print('|                                            |')
        print('|    ____________    |_')
        print('|   |                                    |   |_)')
        print('|   |   8         4         2         1  |   |')
        print('|   |                                    |   |')
        print(f'|   |   {vetor_hora[0]}         {vetor_hora[1]}         {vetor_hora[2]}         {vetor_hora[3]}  |   |')
        print('|   |                                    |   |')
        print('|   |                                    |   |')
        print(f'|   |   {vetor_minuto[0]}     {vetor_minuto[1]}     {vetor_minuto[2]}     {vetor_minuto[3]}     {vetor_minuto[4]}     {vetor_minuto[5]}  |   |')
        print('|   |                                    |   |')
        print('|   |   32    16    8     4     2     1  |   |_')
        print('|   |____________|   |_)')
        print('|                                            |')
        print('|________________|')
        print()

    except EOFError:
        break