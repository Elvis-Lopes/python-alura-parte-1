import random

numero_secreto = random.randint(1, 10)

print('-=' * 17)
print('Bem-vindo ao jogo de adivinhação!')
print('-=' * 17)

numero = int(input("chuta um número de 1 a 10: "))

if numero == numero_secreto:
    print("Acertou!!!")
else:
    print("Errou")

print(f'O numero da maquina é {numero_secreto}')