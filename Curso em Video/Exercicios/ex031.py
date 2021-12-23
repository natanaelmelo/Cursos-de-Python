# Exercício Python 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

distancia = float(input('Qual a distancia da sua viagem em km: '))

if distancia < 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

print(f'Como sua viagem tem cerca de {distancia:.2f} km, o preço da passagem é de R$ {passagem:.2f}!')