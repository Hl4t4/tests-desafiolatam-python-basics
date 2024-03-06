from timing import pizza_timing

def add_ingrediente(pizza, ingrediente):
    new_pizza = pizza
    if new_pizza['ingredientes'].get(ingrediente) != None:
        new_pizza['ingredientes'][ingrediente] = True
        new_pizza = pizza_timing(new_pizza)
    else:
        print(f"{ingrediente} es un ingrediente invalido")
    return new_pizza

def add_ingredientes(pizza, ingredientes):
    new_pizza = pizza
    for ingrediente in ingredientes:
        new_pizza = add_ingrediente(new_pizza, ingrediente)
    return new_pizza