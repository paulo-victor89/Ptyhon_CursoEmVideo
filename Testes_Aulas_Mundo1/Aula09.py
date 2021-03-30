frase = 'Curso em Vídeo Python'
'''mostra a frase completa'''
print(frase)
''' fatiando, mostra somente a letra informada'''
print(frase[3])
''' fatiando, mostra da letra 3 até a 13, não incluindo a 13 letra'''
print(frase[3:13])
''' fatiando, mostra do inicio até a 13, não incluindo a 13 letra'''
print(frase[:13])
''' fatiando, mostra do 13 até o final'''
print(frase[13:])
''' fatiando, mostra da letra 1 até a 15, não incluindo a 15 letra'''
print(frase[1:15])
''' fatiando, mostra da letra 1 até a 15,pulando de 2 em 2 não incluindo a 15 letra'''
print(frase[1:15:2])
''' fatiando, mostra da letra 1 até a final,pulando de 2 em 2 '''
print(frase[1::2])
''' fatiando, mostra do inicio até o final,pulando de 2 em 2 '''
print(frase[::2])
''' fatiando, mostra da letra 1 até a final,pulando de 2 em 2 '''
print(frase[1::2])
'''para escrever texto longo, e assim: print( """ digite o texto """) 
muito util para fazer menus
'''
''' contando a quantidade de um determinado caractere, percorrendo toda a string, lembrando que tem diferença entre maiusculas e minusculas nesse caso aqui '''
print(frase.count('o'))

''' contando a quantidade de um determinado caractere, percorrendo toda a string, transformando as letras em maiusculas contando as maiusculas'''
print(frase.upper().count('O'))
''' contando a quantidade de caracteres contidos na string, espaço conta'''
print(len(frase))
''' contando a quantidade de caracteres contidos na string, retiando os espaços'''
print(len(frase.strip()))
''' trocando python por android'''
print(frase.replace('Python', 'Android'))
''' verificando se existe uma palavra dentro da string'''
print('Curso'in frase)
''' mostra a posição inicial do conteudo pedido'''
print(frase.find('Curso'))
''' fazendo a busca e colocando todas as letras minusculas'''
print(frase.lower().find('vídeo'))
'''fazendo a divisão e criando uma lista'''
print(frase.split())
'''fazendo a divisão, criando uma lista e mostrando somente uma posição'''
dividido = frase.split()
print(dividido[0])
'''fazendo a divisão, criando uma lista e mostrando somente uma letra contida na palavra'''
dividido = frase.split()
print(dividido[2][3])