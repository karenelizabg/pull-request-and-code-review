import random

def main():
    print("¡Bienvenido al juego de adivinar el número!")
    print("===============================")
    print("Estoy pensando en un número entre 1 y 20.")
    print("¿Puedes adivinar cuál es?")

    startGame()


def generateNumber():
    return random.randint(1, 20)

def checkGuess(guess, number):
    if guess < number:
        return "Muy bajo"
    elif guess > number:
        return "Muy alto"
    elif guess == number:
        return "¡Correcto!"
    
def startGame():
    number = generateNumber()
    guess = 0
    attempts = 0

    while guess != number:
            guess = int(input("Introduce numero: "))
            attempts += 1
            print(checkGuess(guess, number))
    
    print("Número de intentos:", attempts)

main()