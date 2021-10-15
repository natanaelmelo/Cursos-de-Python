# Exercício Python 28
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print('Vou pensar em um número inteiro entre 0 e 5 e tente adivinha!')
n = int(input('Qual é o seu palpite: '))  # Usuário entra com um número
comp = randint(0, 5)  # Faz o computador pensar em um número aleatorio entre 0 e 5

if comp == n:  # Se o usuário acertar o número que o computador pensou
    print('Parabéns, você acertou o número que eu pensei!!!')
else:  # Se o usuário errar o número que o computador pensou
    print('Ops, você errou... Tente de novo!!!')