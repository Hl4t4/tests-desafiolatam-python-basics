def change_masa(pizza, new_masa, masas):
    """Esta funcion cambia el tipo de masa de la pizza recibida
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    new_masa: [str]
        Nueva masa a agregar
    masas: [list]
        Lista de masas disponibles en la tienda
    Returns
    ----------
    [dictionary]
        Retorna la pizza con la masa cambiada en caso de ser valida la recibida
    """
    new_pizza = pizza
    change = [masa for masa in masas if masa.lower() == new_masa.lower()]
    if len(change) >= 1:
        print(f"Se cambio el tipo de masa de {new_pizza['masa']} a {change[0]}")
        new_pizza["masa"] = change[0]
    else:
        print(f"La masa {new_masa} no es una masa valida")
        print(f"Probar con {masas}")
    return new_pizza

def change_salsa(pizza, new_salsa, salsas):
    """Esta funcion cambia el tipo de salsa de la pizza recibida
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    new_salsa: [str]
        Nueva salsa a agregar
    masas: [list]
        Lista de salsas disponibles en la tienda
    Returns
    ----------
    [dictionary]
        Retorna la pizza con la salsa cambiada en caso de ser valida la recibida
    """
    new_pizza = pizza
    change = [salsa for salsa in salsas if salsa.lower() == new_salsa.lower()]
    if len(change) >= 1:
        print(f"Se cambio el tipo de salsa de {new_pizza['salsa']} a {change[0]}")
        new_pizza["salsa"] = change[0]
    else:
        print(f"La salsa {new_salsa} no es una salsa valida")
        print(f"Probar con {salsas}")
    return new_pizza