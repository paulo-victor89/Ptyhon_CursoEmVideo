'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
ex: Digite um numero: 1834

 unidade: 4
 dezenas: 3
 centenas: 2
 milhar: 1
'''
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Analisando o numero: {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))