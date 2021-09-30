# Exercício Python 14
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Qual é a temperatura em °C: '))

fah = (cel * 1.8) + 32

print(f'{cel:.1f} °C é o mesmo que {fah:.1f} °F')

