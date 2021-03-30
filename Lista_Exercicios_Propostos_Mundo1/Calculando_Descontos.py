'''ex 12 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto '''
''' 
produto = float(input('Digite o valor do produto? R$ '))
desconto = produto - (produto * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(produto,desconto))
'''

# Aqui e possivel colocar qualquer % de desconto
produto = float(input('Digite o valor do produto? R$ '))
porcentagem = float(input('Qual a porcentagem de desconto % '))
desconto = (produto * (porcentagem / 100))
pd = produto - desconto

print('O valor do produto era R$ {:.2f} recebeu um desconto, de {}%, e ficou por R${:.2f}'.format(produto,porcentagem, pd))
