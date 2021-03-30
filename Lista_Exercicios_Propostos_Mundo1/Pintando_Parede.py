'''ex 11 Faça um programa que leia altura largura e altura altura de uma parede em metros, calcule altura sua area e altura quantidade
de tinta necessária para pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m²(quadrados).
'''
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem altura dimensão de {} x {} e sua área e de {}m²'.format(largura, altura, area))
print('E necessário {}L de tinta para pintar essa parede'.format(tinta))
