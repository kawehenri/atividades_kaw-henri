# Atividade 4

''' Crie um sistema que receba o nome do usuário, a idade só podendo aceitar numero inteiro, 
em seguida mostre o nome e idade do usuário e peça que ele digite 2 números para que sejam somados. 
Mostrar por último a soma realizada para o usuário.

'''

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print("Seu nome é: ", nome)
print("Sua idade é: ", idade)

num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
soma = num1 + num2 # Soma dos números que irá gerar o resultado
print(f'A soma dos números escolhidos é: {soma}')