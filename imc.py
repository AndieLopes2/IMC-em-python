#Criando um programa para calcular o IMC

#Entrada dos dados (Interação com o usuário)

nome = input(str("Olá, qual é o seu nome? "))
print(f'\nSeja bem vindo(a), {nome}! Gostaríamos de calcular o seu IMC.\n')
massa = float(input('Qual é a sua massa? '))
altura = float(input('Qual é a sua altura? '))

#Processamento (cálculo do IMC)

imc = float(massa / (altura ** 2))

#Saída dos dados (Usando valores da tabela IMC)

print(f'\nO seu IMC é: {imc:.2f} \n')

if(imc <= 16.9):
    print('Você está muito abaixo do peso adequado de acordo com a tabela IMC.')
elif(imc <= 18.4 and imc >= 17):
    print('Vocé está abaixo do peso adequado de acordo com a tabela IMC. ')
elif(imc <= 24.9 and imc >= 18.5):
    print('Seu peso é adequado de acordo com a tabela IMC.')
elif(imc <= 34.9 and imc >= 30):
    print('Você possui obesidade grau 1 de acordo com a tabela IMC.')
elif(imc <= 40 and imc >= 35):
    print('Você possui obesidade grau 2 de acordo com a tabela IMC.')
else:
    print('Você possui obesidade grau 3 ou mórbida, de acordo com a tabela IMC.')
