'''ex: 4
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo(type) e todas as informações possiveis sobre ele'''

a = input('Digite algo:')

input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(a)}')

print(f'Só tem espaços? {a.isspace()}')

print(f'É um número? {a.isnumeric()}')

print(f'É alfabético? {a.isalpha()}')

print(f'É alfanumérico? {a.isalnum()}')

print(f'Está em maiúsculas? {a.isupper()}')

print(f'Está em minúsculas? {a.islower()}')

print(f'Está capitalizado? {a.istitle()}')
