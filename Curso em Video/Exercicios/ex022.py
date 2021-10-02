# Exercício Python 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome completo: ')).strip()
nomed = nome.split()

print(f'Seu nome com todas as letras maiusculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minusculas é: {nome.lower()}')
print(f'Seu nome completo tem {len("".join(nomed))} letras')
print(f'Seu primeiro nome tem {len(nomed[0])} letras')
