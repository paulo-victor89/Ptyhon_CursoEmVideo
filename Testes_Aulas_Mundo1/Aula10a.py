n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
print('A sua média foi {:.1f}'.format(media))
if media>= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

'''Executando uma condição simplificada'''
print('Parabéns!' if media>=6 else 'Estude mais!')
