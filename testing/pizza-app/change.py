def change_masa(pizza, new_masa, masas):
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
    new_pizza = pizza
    change = [salsa for salsa in salsas if salsa.lower() == new_salsa.lower()]
    if len(change) >= 1:
        print(f"Se cambio el tipo de salsa de {new_pizza['salsa']} a {change[0]}")
        new_pizza["salsa"] = change[0]
    else:
        print(f"La salsa {new_salsa} no es una salsa valida")
        print(f"Probar con {salsas}")
    return new_pizza