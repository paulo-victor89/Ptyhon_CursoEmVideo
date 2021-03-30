'''Desafio 29
   - Escreva um programa que leia a velocidade de um carro:
    - Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    - A multa vai custar R$ 7,00 por cada KM acima do limite
'''
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite de velocidade que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Foi multado, em R${:.2f}'.format(multa))
else:
    print('Tenha uma boa viagem, dirija com segurança!')
