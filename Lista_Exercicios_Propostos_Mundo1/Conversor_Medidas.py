'''ex: 8 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros'''
metros = float(input('Digite o valor em metros que deseja converter: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'O valor de {metros} M corresponde altura {centimetros} CM e {milimetros} MM')

'''Solução do Gustavo Guanabara
print('A media de {}m correponde altura {:.0f}cm e {:.0f}mm'.format(metros, centimetros, milimetros))
Assim o resulta não apresenta casas decimais após altura virgula, facilitando altura leitura do valor.
O {:.0f} so e aconselhavel colocar nos resultados.
'''