def valid_action (action):
    match action:
        case "Si" | "No":
            return True
        case _:
            return False

def input_action (input_text):
    action = input(input_text).capitalize()
    while (not valid_action(action)):
        action = input("Valor invalido, debe ser si o no.\n")
    return action
        


first_action = input_action("Responde a estimulos?\n")
if (first_action == "Si"):
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
else:
    second_action = input_action("Respira?\n")
    if (second_action == "Si"):
        print("Permitirle posicion de suficiente ventilacion")
    else:
        print("Administrar 5 Ventilaciones y llamar a ambulancias")
        while (True):
            third_action = input_action("Signos de vida?\n")
            if (third_action == "Si"):
                print("Reevaluar la espera de la ambulancia")
            else:
                print("Administrar comprensiones toracicas hasta que llegue la ambulancia")
            forth_action = input_action("Llego la ambulancia?\n")
            if (forth_action == "Si"):
                break
print("FIN")