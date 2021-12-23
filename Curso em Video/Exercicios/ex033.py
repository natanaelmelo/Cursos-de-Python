# Exercício Python 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Me diga um número: '))
n2 = int(input('Me diga mais um número: '))
n3 = int(input('Me diga só mais um número: '))

# Verificando qual é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando qual é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'\nO maior número é o {maior} e o menor número é {menor}')
