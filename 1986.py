# -*- coding: utf-8 -*-

n = int(input())
msg = input().split()

for i in range(len(msg)):
    # Converte a entrada em hexadecimal para decimal do tipo inteiro
    decimal = int(msg[i], 16)
    # O inteiro decimal para um caractere da tabela ASCII
    char = chr(decimal)
    msg[i] = char
print(''.join(msg))