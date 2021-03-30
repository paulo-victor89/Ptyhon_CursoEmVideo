'''Crie um programa que leia um numero inteiro e mostre na tela se e par ou impar'''
numero = int(input('Digite um número qualquer: '))
if numero % 2 == 0: # o resto da divisão do número = 0
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))# o resto da divisão do número = 1
