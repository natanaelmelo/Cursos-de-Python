# Exercício Python 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Parabéns você ganhou um desconto de 5% na compra de qualquer produto')

preco = float(input('Qual é o valor do produto: R$ '))
preco = preco - (preco * 0.05)

print(f'O produto agora custa R$ {preco:.2f}')
