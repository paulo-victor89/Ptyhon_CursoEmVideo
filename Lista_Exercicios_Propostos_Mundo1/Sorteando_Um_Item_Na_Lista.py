''' O professor quer sortear um dos seus 4 alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido'''
from random import choice
n1 = (input('Digite o nome do primeiro aluno: '))
n2 = (input('Digite o nome do segundo aluno: '))
n3 = (input('Digete o nome do terceiro aluno: '))
n4 = (input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi: ',escolhido)