'''ex 13 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento'''

salario = float(input('Digite o salario do funcionário? R$ '))
novoSalario = salario + (salario * 15 / 100)
print('O funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario,novoSalario))

'''
# Aqui e possivel colocar qualquer % de acrescimo
salario = float(input('Digite o salario do funcionário? R$ '))
porcentagem = float(input('Quanto ele vai receber de aumento?  % '))
novoSalario = (salario + (salario * porcentagem / 100))

print('O funcionário que ganhava R$ {:.2f} recebeu um aumento, de {}%, e passa a receber R${:.2f}'.format(salario,
                                                                                                          porcentagem,
                                                                                                          novoSalario))
'''