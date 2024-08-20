# Atividade 3

'''

    Crie um sistema onde o usuário irá inserir dois valores, guarde cada valor em variáveis, 
em seguida vocês irão realizar as 4 operações básicas de matemática (+; -; *, /) e mostrar esses 
resultados na tela, também concatenados a um texto indicativo de cada operação.

'''
num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))

soma = num1 + num2 # Soma dos números que irá gerar o resultado
multi = num1 * num2 # Subtração dos números que irá gerar o resultado
div = num1 / num2 # Multiplicação dos números que irá gerar o resultado
sub = num1 - num2 # Divisão dos números que irá gerar o resultado

print(f'A soma dos números escolhidos é: {soma}')
print(f'A subtração dos números escolhidos é: {sub}')
print(f'A divisão dos números escolhidos é: {div:.2f}')
print(f'A multiplicação dos números escolhidos é: {multi} ')