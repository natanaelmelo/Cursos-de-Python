# Exercício Python 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Me fale um número de 0 a 9999: '))

print(f'Analisando o número {n}, temos: ')

u = n % 10
print(f'Unidades: {u}')

n = (n - u) / 10
d = n % 10
print(f'Dezenas: {d:.0f}')

n = (n - d) / 10
c = n % 10
print(f'Centenas: {c:.0f}')

n = (n - c) / 10
m = n % 10
print(f'Milares: {m:.0f}')