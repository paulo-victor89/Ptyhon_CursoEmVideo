''''''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
multiplicação = n1 * n2
divisao = n1 / n2
divisaoInteiro = n1 // n2
potencia = n1 ** n2

print(f"Soma ={soma}, A multiplicação = {multiplicação}", end=' ')
print(', Divisão ={:.2f}'.format(divisao), end=' ')
print(f', Divisão inteira ={divisaoInteiro} , É a potência={potencia}')
