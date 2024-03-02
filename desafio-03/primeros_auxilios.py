# Funcion para validar si es una accion valida o no
def valid_action (action):
    match action:
        case "Si" | "No":
            return True
        case _:
            return False

# Funcion para ingresar acciones donde se comprueba si es valida con valid_action
def input_action (input_text):
    action = input(input_text).capitalize()
    while (not valid_action(action)):
        action = input("Valor invalido, debe ser si o no.\n")
    return action
        

# Pasos que sigue el diagrama entregado de acciones a seguir, incluido el ciclo en la tercera y cuarta accion
first_action = input_action("¿Responde a estimulos?\n")
if (first_action == "Si"):
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
else:
    second_action = input_action("¿Respira?\n")
    if (second_action == "Si"):
        print("¿Permitirle posicion de suficiente ventilacion")
    else:
        print("Administrar 5 Ventilaciones y llamar a ambulancias")
        while (True):
            third_action = input_action("¿Signos de vida?\n")
            if (third_action == "Si"):
                print("Reevaluar la espera de la ambulancia")
            else:
                print("Administrar comprensiones torácicas hasta que llegue la ambulancia")
            forth_action = input_action("¿Llego la ambulancia?\n")
            if (forth_action == "Si"):
                break
print("FIN")