'''ex:15
Faca um programa que pergunte a quantidade de km percorridos por um carro alugado.
A quantidade de dias pelos quais ele foi alugado.
Calcule o preco a pagar.
Sabendo que o carro custa R$60 por dia,
R$ 0,15 por km rodado.
'''
dias = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de KM percorridos: '))
diaAlugado = dias * 60
kmPercorrido = km * 0.15
preco = diaAlugado + kmPercorrido

print('O carro foi alugado por {} dias, com preco total de R$ {:.2f}'.format(dias, diaAlugado))
print('Foram percorridos {:.0f} KM, com custo total de R${:.2f}'.format(km, kmPercorrido))
print('O total a pagar e de R${:.2f}'.format(preco))
