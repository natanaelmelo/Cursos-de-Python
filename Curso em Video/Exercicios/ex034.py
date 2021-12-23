# Exercício Python 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salario: '))

if salario <= 1250:
    salario = salario + (salario * 0.15)
    print(f'O seu novo salário é de R$ {salario:.2f}')
else:
    salario = salario + (salario * 0.1)
    print(f'O seu novo salario é de R$ {salario:.2f}')