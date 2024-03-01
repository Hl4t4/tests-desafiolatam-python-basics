import random
import argparse

def valid_play (play):
    match play:
        case "Piedra" | "Papel" | "Tijera":
            return True
        case _:
            return False
        
def cachipun_value_converter (play):
    match play:
        case "Piedra":
            return 1
        case "Papel":
            return 2
        case "Tijera":
            return 3

def cachipun (play):
    play_value = cachipun_value_converter(play)
    computer_play = random.choice(["Piedra", "Papel", "Tijera"])
    computer_play_value = cachipun_value_converter(computer_play)

    print("Tu jugaste "+ play)
    print("Computador jugo "+ computer_play)

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
    parser = argparse.ArgumentParser(description="Calculadora IMC ingresar peso en Kg y altura en cm") # add description later
    parser.add_argument("play")
    args = parser.parse_args()

    play = args.play
    play = play.capitalize()

    if valid_play(play):
        cachipun(play)
    else: 
        print("Argumento invalido: debe ser piedra, papel o tijera.")