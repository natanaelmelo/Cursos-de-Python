# Exercício Python 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km você percorreu com esse carro: '))
dias = int(input('Por quantos dias ele foi alugado: '))

alguel = (dias * 60) + (km * 0.15)

print(f'Como você alugou o carro por {dias} dias e percorreu {km} km, o valor do aluguel a ser pago é de R$ {alguel:.2f}.')
