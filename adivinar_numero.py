# Juego de adivinar el número
import random


RANGO_INICIAL = 1
RANGO_FINAL_FACIL = 25
RANGO_FINAL_MEDIO = 150
RANGO_FINAL_DIFICIL = 300


def main():
    """Mensaje de bienvenida y arranque del juego."""
    print("============================================")
    print("¡Bienvenido al juego de adivinar el número!")
    print("============================================")

    iniciar_juego()


def seleccionar_dificultad():
    """Selecciona la dificultad del juego."""
    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil (1-25)")
        print("2. Medio (1-150)")
        print("3. Difícil (1-300)")
        print("4. Personalizado")
        opcion = input("\nOpción:\n    > ")

        if opcion == '1':
            return RANGO_INICIAL, RANGO_FINAL_FACIL
        elif opcion == '2':
            return RANGO_INICIAL, RANGO_FINAL_MEDIO
        elif opcion == '3':
            return RANGO_INICIAL, RANGO_FINAL_DIFICIL
        elif opcion == '4':
            return seleccionar_rango()
        else:
            print("Por favor, selecciona una opción válida.")


def seleccionar_rango():
    """Permite al usuario seleccionar un rango personalizado para el número a adivinar."""
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


def generar_numero(rango_inicial, rango_final):
    """Genera un número aleatorio dentro del rango especificado."""
    return random.randint(rango_inicial, rango_final)


def comprobar_intento(intento, numero):
    """Compara el intento del usuario con el número a adivinar y devuelve una pista."""
    if intento < numero:
        return f"¡BAJO! El número es más alto que {intento}\n"
    elif intento > numero:
        return f"¡ALTO! El número es más bajo que {intento}"
    elif intento == numero:
        return f"¡CORRECTO! El número es {numero}\n"


def iniciar_juego():
    """Inicia el juego de adivinar el número."""
    rango_inicial, rango_final = seleccionar_dificultad()
    numero = generar_numero(rango_inicial, rango_final)
    adivinanza = 0
    intentos = 0
    
    print(f"\nEstoy pensando en un número entre {rango_inicial} y {rango_final}")
    print("¿Puedes adivinar cuál es?")

    while adivinanza != numero:
        try:
            adivinanza = int(input("\nIntroduce número:\n    > "))
            intentos += 1
            print(comprobar_intento(adivinanza, numero))
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    print("Número de intentos:", intentos)


if __name__ == "__main__":
    main()