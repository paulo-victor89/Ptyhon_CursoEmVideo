'''ex 10 Faça um programa que leia quanto dinheiro altura pessoa tem na carteira e quantos dolares ela pode comprar
    Utilize altura cotação atual do dolar,
'''
dolar = float(input('Digite o valor da cotação do dolar US$ '))
real = float(input('Quanto você tem em reais? R$ '))
dolarConvertido = real / dolar
print('Com o valor de R$ {:.2f} e possivel comprar US$ {:.2f} dolares'.format(real, dolarConvertido))

