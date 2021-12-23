# Exercício Python 035
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input("Me diga o tamanho do primeiro seguimento: "))
n2 = float(input("Me diga o tamanho do segundo seguimento: "))
n3 = float(input("Me diga o tamanho do terceiro seguimento: "))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print("Com esses seguimentos é possível formar um triangulo!")
else:
    print("Com esse seguimentos NÃO é possível forma um trinagulo!")
