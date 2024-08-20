# Atividade 01:
'''
    Criar um sistema para receber o nome, idade, peso, altura
    Converter a idade para receber somente números inteiros
    Imprimir os tipos de dados
    Imprimir todas as informações concatenadas usando f string
'''
#variaveis e seus tipos de dados 
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

peso = input('Digite o seu peso: ')
peso = float(peso) #conversão afim de o usário possa digitar de qualquer maneira

altura = input('Digite a sua altura:')
altura = float(altura)

print(f'O seu nome é {nome}, você possui {idade} anos, pesa {peso}Kg e tem {altura} de altura.')
