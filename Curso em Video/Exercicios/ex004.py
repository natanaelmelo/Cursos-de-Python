# Exercício Python 4
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = input('Me fale uma frase: ')

print('O tipo primitvo é ', type(frase))
print('É somente espaço: ', frase.isspace())
print('É númerico: ', frase.isnumeric())
print('É alfabetico: ', frase.isalpha())
print('É alfanumerico: ', frase.isalnum())
print('Está em maiuscula: ', frase.isupper())
print('Está em minuscula: ', frase.islower())
print('Está em capitalizada: ', frase.istitle())
