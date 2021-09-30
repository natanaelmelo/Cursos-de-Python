# Exercício Python 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Me fale um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'O número informado é {n}, o dobro desse número é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.0f}!')

