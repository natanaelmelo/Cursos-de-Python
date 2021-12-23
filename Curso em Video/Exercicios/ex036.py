# Exercício Python 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa: '))
anos = int(input('Por quantos anos irá pagar a casa: '))
salario = float(input('Qual é o seu salario: '))

prestacao = casa / (anos * 12)

minimo = salario * 0.3

print(f'Para pagar um casa no valor de R$ {casa:.2f} em {anos} anos', end=' ')
print(f'a prestação será de R$ {prestacao:.2f}')

if prestacao <= minimo:
    print(f'Emprestimo aprovado. Agora você poderá comprar sua casa!')
else:
    print(f'Emprestimo negado. Você não poderá comprar sua casa!')