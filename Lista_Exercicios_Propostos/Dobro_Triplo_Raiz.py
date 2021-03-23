'''ex:6 Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada'''
print('Calculando o dobro, triplo e altura raiz quadrada de um numero!')
n = int(input('Digite um numero: '))

print(f"O Dobro de {n} = {n*2},\nO Triplo de {n} = {n*3}", end=' ')
print(',\nRaiz Quadrada de = {:.2f}'.format(n**(1/2)), end=' ')

# Solução do Gustavo Guanabara
#print('O dobro de {} vale {}, \nO triplo de {} vale {},\nA raiz quadrada de {} é igual altura {:.2f}'.format(n,(n*2),n,(n*3),n,(n**(1/2))))
# outra forma de calcular raiz e pow(n,(1/2))