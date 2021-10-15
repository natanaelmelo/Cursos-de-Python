# Exercício Python 29
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = float(input('Qual é a velocidade do carro: '))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você ultrapassou o limite de 80Km/h e deve pagar uma multa de R$ {multa:.2f}')
else:
    print('Você está dentro do limite, pode continuar!')
    