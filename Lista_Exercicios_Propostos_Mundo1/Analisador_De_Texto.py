'''Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiusculas

- O nome com todas as letras minusculas

- Quantas letras ao todos(sem considerar espaços)

- Quantas letras tem o primeiro nome

'''
nome = str(input('Digite o seu nome completo: ').upper().strip())
print ('Analisando seu nome: ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')))
primeiroNome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))

