# Exercício Python 37
# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Me diga um número inteiro qualquer: '))
print('Escolha para qual base deseja converter o número a cima: \n[1] Binario \n[2] Octal \n[3] Hexadeciaml')
x = int(input('Opção desejada: '))

if x == 1:
    print(f'O número {n} em bínario é {bin(n)[2:]}!')
elif x == 2:
    print(f'O número {n} em octal é {oct(n)[2:]}!')
else:
    print(f'O número {n} em hexacimal é {hex(n)[2:]}!')
