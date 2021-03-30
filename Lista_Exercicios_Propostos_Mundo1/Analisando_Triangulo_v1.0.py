'''Desafio 35
- Faça um programa que leia 3 segmentos de reta  e diga se esses valores formam um triangulo
se o r1 for menor que a soma dos outros 2 segmentos
'''
print('-=' * 20)
print('Analisador de triangulos:')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 <r2 +r3 and r2<r1+r3 and r3<r1 + r2:
    print('Os segmentos digitados PODEM FORMAR um triângulo')
else:
    print('Os segmentos digitados NÃO PODEM FORMAR um triângulo')