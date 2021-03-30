''' desafio 31
Desenvolva um programa que pergunte a distancia de uma viagem em KM.
    Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200KM.
    Cobrar R$ 0,45 para viagens acima de 200KM.
'''
distancia = float(input('Qual a distancia da sua viagem? '))
# valor = distancia * 0.50 if distancia <=200 else distancia *0.45
# no caso acima e um if simplificado, deve apresentar o mesmo valor
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
    print('O preço da sua passagem será R$ {:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('O preço da sua passagem será R$ {:.2f}'.format(valor))
