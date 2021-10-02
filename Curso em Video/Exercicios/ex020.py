# Exercício Python 20
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]

# sorteados = random.sample(alunos, k=4)

"""
O bom de usar o sample ao invés do shuffle é que da para limitar a quantidade de pessoas que vão apresentar, 
atribuindo a quantidade no 'k', então se na lista tiverem 10 alunos inscritos 
mas o k for igual a 5, então serão escolhidos apenas 5 dentre os 10 alunos
"""

random.shuffle(alunos)

print(f'A ordem de apresentação será:')
print(alunos)  # Caso queira usar sample, printe sorteados
