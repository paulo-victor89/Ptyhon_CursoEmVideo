'''Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo(type) e todas as informações possiveis sobre ele'''

n = input('Digite algo:')

digitados = n


print("Qual e o tipo primitivo desse valor? ",type(n))
print("É um numero? ",n.isnumeric())
print("É uma letra? ",n.isalpha())
print("É um alfanumerico? ",n.isalnum())
print("Esta somente com letras maiusculas? ",n.isupper())
print("Esta somente com letras minusculas? ",n.islower())


