import random

numero_aleatorio = random.randint(1, 10)
numero_tentativas = 0

while True:
    numero_usuario = int(input("Digite um número: "))
    numero_tentativas += 1
    if numero_usuario > numero_aleatorio:
        print("Muito Alto!")
    elif numero_usuario < numero_aleatorio:
        print("Muito baixo!")
    elif numero_usuario == numero_aleatorio:
        print(f"Acertou! Você precisou de {numero_tentativas} tentativas.")
        break



