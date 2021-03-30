''' Desafio 28
   - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
   - o usuário tentar descobrir quaal foi o número escolhido pelo computador.
   - O programa deverá escrever na tela se o usuario venceu ou perdeu.
 '''
import random
from random import randint
from time import sleep
computador = randint(0,5)# faz o computador sortear o número
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('-=-'* 20)
print('Pense em um número de 0 a 5...')
jogador=int(input('Em que número eu pensei?  '))# jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Perdeu, eu pensei no número {}, e não {} '.format(computador, jogador))