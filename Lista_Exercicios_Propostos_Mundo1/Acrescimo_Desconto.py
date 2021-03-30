'''ex extra: Crie um algoritmo que leia o valor de um produto e mostre  o valor dele com desconto e acrescimo
Pagamento a vista: recebe desconto de 10%
Pagamaneto a prazo: acrescimo de 5%
'''
produto = float(input('Digite o valor do produto: '))
desconto = produto - (produto * 10 / 100)
acrescimo = produto + (produto * 5 / 100)

print('O valor do produto é R$ {},\na vista com desconto fica R$ {} ,\na prazo fica R$ {} '.format(produto, desconto,
                                                                                                 acrescimo))
