'''
Desafio 16
- Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um número: 6.127
O número 6.217 tem a parte inteira 6
'''

from math import floor
num = float(input('Digite um número: '))
inteira = floor(num)
print('O número {} tem a parte inteira = {:.0f} '.format(num, inteira))

from math import trunc
numero = float(input("Digite um número: "))
print("A parte inteira do número é {}".format(trunc(numero)))