#ler numero 1 e 2 e passar para inteiro
num1, num2 = input().split()
num1, num2 = int(num1), int(num2)

#fazer repetição do número diminuindo 1 a cada for até encontrar um que atenda a condição
for i in range(num1, -1, -1):
    #2 é o menor número primo, então tem que ser maior que ele
    if num1 >= 2:
        #verificar se número digitado será divisível pelos números
        #naturais maiores iguais a 2 (para ser primo) e menores que o número
        #i (número da repetição)
        for j in range(2, i):
            #se a divisão for exata número não é primo
            # se não tiver divisão exata o número cai no else e é primo
            if (i % j) == 0:
                break
            #pega o primeiro número primo em ordem decrescente
        else:
            primo1 = i
            break
        
#repete procedimento para o segundo número           
for i in range(num2, -1, -1):
    if num2 >= 2:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else :
            primo2 = i
            break
        
#multiplicação de números primos e printa resultado
r = primo1*primo2
print(r)