import random
import argparse # Libreria usada para obtener argumentos del inicio de la aplicacion

# Verificacion si es una jugada valida
def valid_play (play):
    match play:
        case "Piedra" | "Papel" | "Tijera":
            return True
        case _:
            return False

# Convertidor a valores int para futuras comparaciones
def cachipun_value_converter (play):
    match play:
        case "Piedra":
            return 1
        case "Papel":
            return 2
        case "Tijera":
            return 3

#Funcion principal con la logica del juego
def cachipun (play):
    #Obtencion de la jugada del computador
    computer_play = random.choice(["Piedra", "Papel", "Tijera"])

    #Se convierten a int para comparar los resultados
    play_value = cachipun_value_converter(play)
    computer_play_value = cachipun_value_converter(computer_play)

    #Impresion de los valores de las jugadas para informacion del usuario
    print("Tu jugaste "+ play)
    print("Computador jugo "+ computer_play)

    #Logica del juego usada en ints debido a la facilidad de comparacion de estos vs strings
    if (play_value < computer_play_value):
        if (play_value == 1 and computer_play_value == 3):
            print("Ganaste!!")
        else:
            print("Perdiste :(")
    elif (play_value == computer_play_value):
        print("Empataron :O")
    else:
        if (play_value == 3 and computer_play_value == 1):
            print("Perdiste :(")
        else:
            print("Ganaste!!")

if __name__ == "__main__":
    #Lectura de argumentos de ingreso
    parser = argparse.ArgumentParser(description="Calculadora IMC ingresar peso en Kg y altura en cm") # add description later
    parser.add_argument("play")
    args = parser.parse_args()

    play = args.play
    play = play.capitalize() #Se capitaliza para que las comparaciones siguientes sean validas

    if valid_play(play): 
        #Caso de que es una jugada valida
        cachipun(play)
    else: 
        #Caso argumento invalido
        print("Argumento invalido: debe ser piedra, papel o tijera.")