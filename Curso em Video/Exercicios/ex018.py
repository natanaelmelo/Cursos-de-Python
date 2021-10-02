# Exercício Python 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tag = math.tan(math.radians(angulo))

print(f'O angulo de {angulo} tem o SENO de {sen:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tag:.2f}')
