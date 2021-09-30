# Exercício Python 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Parabéns você recebeu um aumento de 15%')

salario = float(input('Qual é o seu salario atual: R$ '))
salario = salario + (salario * 0.15)

print(f'O seu salario agora é de R$ {salario:.2f}')
