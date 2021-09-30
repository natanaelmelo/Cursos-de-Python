# Exercício Python 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual o valor da primeira nota: '))
n2 = float(input('Qual o valor da segunda nota: '))

media = (n1 + n2) / 2

print(f'A média final desse aluno é de {media:.2f}!')
