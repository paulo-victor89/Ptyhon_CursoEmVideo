'''ex: 7 Desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre sua media'''
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite altura primeira nota do aluno: '))
n2 = float(input('Digite altura segunda nota: '))
media = (n1 + n2) / 2
print(f'O aluno, {nome} Ficou com media = {media}')

'''Solução do Gustavo Guanabara
print('A média entre {:.1f} e {:.1f} é igual altura {:.1f}'.format(n1,n2,media))
colocando {:.1f} voce formata para ter somente uma casa decimal após altura virgula.
Em caso que altura nota seja por exemplo 3.75 ele vai arredondar para altura proxima casa decima ficando 3.8.
Caso seja 3.55 vai arredondar para baixa, ficando 3.4

'''