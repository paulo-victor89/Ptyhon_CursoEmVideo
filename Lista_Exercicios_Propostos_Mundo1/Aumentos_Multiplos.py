'''
  - Desafio 34
    Escreva um programa que pergunte o salário de um funcionário.
    Calcule o valor do seu aumento
        Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
    Para os inferiores ou iguais, o aumento e de 15%
  '''

salario = float(input("Digite o salário do funcionário R$ "))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
    print('De acordo com o salário, o funcionário vai receber um aumento de 15%')
else:
    novoSalario = salario + (salario * 10 / 100)
    print('De acordo com o salário, o funcionário vai receber um aumento de 10%')
print('O funcionário que ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'.format(salario, novoSalario))
