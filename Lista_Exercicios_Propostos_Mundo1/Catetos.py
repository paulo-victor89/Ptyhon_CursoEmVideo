''' Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjancente: '))
hi = hypot(co, ca)
print('Com o cateto oposto medindo {} e o cateto adjacente medindo {} o valor da hipotenusa é {:.2f} '.format(
    co, ca, hi))