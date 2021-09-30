# Exercício Python 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Me fale um valor em metros: '))

cm = m * 100
mm = m * 1000

print(f'{m} m convertido em centímetros é {cm:.0f} cm e convertido em milimetros é {mm:.0f} mm!')
