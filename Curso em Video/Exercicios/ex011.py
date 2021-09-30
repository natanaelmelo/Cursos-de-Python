# Exercício Python 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Qual a largura da parede (em metros): '))
alt = float(input('Qual a altura da parede (em metros): '))

area = larg * alt  # Descobrir a area da parede
tinta = area / 2  # Descobrir a quantidade de tinta necessária

print(f'Como a parede tem {area} m², será necessário {tinta:.2f} litros de tinta para pintá-la.')