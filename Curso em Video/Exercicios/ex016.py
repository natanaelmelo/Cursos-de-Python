# Exercício Python 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

n = float(input('Me diga um número real qualquer: '))

print(f'O número {n} tem a parte inteira {math.trunc(n)}.')
