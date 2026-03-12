import random

def main():
    print("¡Bienvenido al juego de adivinar el número!")
    print("===============================")
    print("Estoy pensando en un número entre 1 y 20.")
    print("¿Puedes adivinar cuál es?")

    iniciar_juego()


def generar_numero():
    return random.randint(1, 20)

def comprobar_adivinanza(intento, numero):
    if intento < numero:
        return "Muy bajo"
    elif intento > numero:
        return "Muy alto"
    elif intento == numero:
        return "¡Correcto!"
    
def iniciar_juego():
    numero = generar_numero()
    intento = 0
    attempts = 0

    while intento != numero:
            intento = int(input("Introduce número: "))
            attempts += 1
            print(comprobar_adivinanza(intento, numero))
    
    print("Número de intentos:", attempts)

main()