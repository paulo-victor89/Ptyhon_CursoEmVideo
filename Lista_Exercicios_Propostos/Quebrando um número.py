'''
- Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.217 tem a parte inteira 6

Usando modulo:
from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira = {:.0f} '.format(num, trunc(num)))
'''
'''Sem modulo'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a parte inteira é {}'.format(num, int(num)))
