''' Desafio 33
    - Faça um programa que leia 3 numeros e mostre qual e o maior e qual o menor
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite segundo número: "))
n3 = int(input("Digite o terceiro número: "))
# Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
