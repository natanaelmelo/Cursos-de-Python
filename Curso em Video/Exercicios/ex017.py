# Exercício Python 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

hi = hypot(co, ca)

print(f'A hipotenusa desse triangulo é de {hi:.2f}.')
