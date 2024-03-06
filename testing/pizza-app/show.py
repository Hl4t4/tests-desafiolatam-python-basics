import os

def show_ingredientes (pizza):
    """Esta funcion entrega los ingredientes de una pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    Returns
    ----------
    [str]
        Retorna el listado de ingredientes como un string separado por comas
    """
    new_pizza = pizza
    ingredientes = [ingrediente for ingrediente, value in new_pizza['ingredientes'].items() if value]
    ingredientes = ", ".join(ingredientes)
    return ingredientes
    # print("Los ingredientes actuales son: ", ingredientes)

def show_menu(ingredientes, salsas, masas, pizza_constructor, change_masa, change_salsa, add_ingrediente, remove_ingrediente, clear):
    """Esta funcion es la encargada de toda la interaccion con el usuario, mostrando las distintas opciones
    Parameters
    ----------
    ingredientes: [list]
        Lista de ingredientes disponibles en la tienda
    salsas: [list]
        Lista de salsas disponibles en la tienda
    masas: [list]
        Lista de masas disponibles en la tienda
    pizza_constructor, change_masa, change_salsa, add_ingrediente, remove_ingrediente: [function]
        Funciones declaradas en otros modulos
    clear: [str]
        string correspondiente al tipo de sistema operativo para limpiar la consola
    """
    print("Bienvenido a la App de Pizzas")
    current_command = input("Desea ordenar una pizza?\n").lower()
    if (current_command == 'si'): #Comprobacion si quiere ingresar a la app
        new_pizza = pizza_constructor(ingredientes) #Se inicia la pizza
        while(current_command != "5"):
            os.system(clear) #Se dan las opciones
            print("Tiene las siguientes opciones:")
            print("Cambiar el tipo de masa [1]")
            print("Cambiar el tipo de salsa [2]")
            print("Agregar un ingrediente [3]")
            print("Quitar un ingrediente [4]")
            print(f"Confirmar con la masa {new_pizza['masa']} con la salsa {new_pizza['salsa']} {show_ingredientes(new_pizza)} [5]")
            current_command = input("Elija entre las opciones [1], [2], [3], [4] y [5]\n O salir de la aplicacion con [exit] o [quit]\n")
            match current_command:
                case "1": #Caso para cambiar el tipo de masa
                    os.system(clear)
                    print(f"Su tipo de masa actual es: {new_pizza['masa']}")
                    new_masa = input(f"Elija un tipo de masa entre {', '.join(masas)}\n")
                    new_pizza = change_masa(new_pizza, new_masa, masas)
                case "2": #Caso para cambiar el tipo de salsa
                    os.system(clear)
                    print(f"Su tipo de salsa actual es: {new_pizza['salsa']}")
                    new_salsa = input(f"Elija un tipo de salsa entre {', '.join(salsas)}\n")
                    new_pizza = change_salsa(new_pizza, new_salsa, salsas)
                case "3": #Caso para agregar un ingrediente dentro de los disponibles
                    os.system(clear)
                    print(f"Sus ingredientes actuales son: {show_ingredientes(new_pizza)}")
                    new_ingrediente = input(f"Elija un ingrediente a agregar entre las siguientes opciones: {', '.join(ingredientes)}\n")
                    new_pizza = add_ingrediente(new_pizza, new_ingrediente)
                case "4": #Caso para remover un ingrediente dentro de los disponibles
                    os.system(clear)
                    print(f"Sus ingredientes actuales son: {show_ingredientes(new_pizza)}")
                    new_ingrediente = input("Elija un ingrediente a eliminar\n")
                    new_pizza = remove_ingrediente(new_pizza, new_ingrediente)
                case "5": #Salida en la que el usuario pide la pizza
                    os.system(clear)
                    print("Gracias por ordenar en App Pizza")
                    print(f"Su pizza con masa: {new_pizza['masa']}")
                    print(f"con salsa: {new_pizza['salsa']}")
                    print(f"con ingredientes: {show_ingredientes(new_pizza)}")
                    print(f"Estara lista en {new_pizza['tiempo']} minutos")
                case "exit" | "quit" | "q" | "Q" | "e" | "E": #Salida de la app sin pedir nada
                    os.system(clear)
                    exit()
                case _:
                    os.system(clear)
                    print("Solo los comandos [1], [2], [3], [4] y [5] son validos en este menu")
    else:
        print("Gracias por venir a la pizzeria")
        exit()