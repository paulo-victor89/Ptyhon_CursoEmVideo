'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente

EX: Paulo Victor Alves Campelo
primeiro: Paulo
ultimo: Campelo
'''
nome =str(input('Digite seu nome completo: ').upper().strip())
# dividindo o nome em espaço, fatiando o nome formando uma lista
n = nome.split()
print('Muito prazer em te conhercer!')
print('O seu primeiro nome e: {}'.format(n[0]))
print('O ultimo nome e: {}'.format(n[len(n)-1]))
