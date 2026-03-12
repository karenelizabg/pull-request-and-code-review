import random

def main():
    print("===============================")
    print("¡Bienvenido al juego de adivinar el número!")
    print("===============================")
    print("\nEstoy pensando en un número entre 1 y 20.")
    print("¿Puedes adivinar cuál es?")

    iniciar_juego()

def seleccionar_rango():
    while True:
        try:
            print("\nSelecciona el rango del número (1-100):")
            rango_inicial = int(input("\nInicio del rango:\n    > "))
            rango_final = int(input("Final del rango:\n    > "))
            if 1 <= rango_inicial <= 100 and 1 <= rango_final <= 100 and rango_inicial <= rango_final:
                return rango_inicial, rango_final
            else:
                print("Por favor, selecciona un número entre 1 y 100.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def generar_numero():
    return random.randint(1, 20)

def comprobar_adivinanza(intento, numero):
    if intento < numero:
        return f"¡BAJO! El número es más alto que {intento}\n"
    elif intento > numero:
        return f"¡ALTO! El número es más bajo que {intento}"
    elif intento == numero:
        return f"¡CORRECTO! El número es {numero}\n"

def iniciar_juego():
    numero = generar_numero()
    intento = 0
    attempts = 0

    while intento != numero:
        try:
            intento = int(input("\nIntroduce número:\n    > "))
            attempts += 1
            print(comprobar_adivinanza(intento, numero))
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    print("Número de intentos:", attempts)

main()