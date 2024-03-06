from timing import pizza_timing

def add_ingrediente(pizza, ingrediente):
    """Esta funcion agrega un ingrediente a la pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    ingrediente: [str]
        Ingrediente que se quiere agregar
    Returns
    ----------
    [dictionary]
        Retorna la pizza con el ingrediente agregado en caso de que existiese
    """
    new_pizza = pizza
    if new_pizza['ingredientes'].get(ingrediente) != None:
        new_pizza['ingredientes'][ingrediente] = True
        new_pizza = pizza_timing(new_pizza)
    else:
        print(f"{ingrediente} es un ingrediente invalido")
    return new_pizza

def add_ingredientes(pizza, ingredientes):
    """Esta funcion agrega un listado de ingredientes a la pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    ingredientes: [list]
        Listado de ingredientes a agregar
    Returns
    ----------
    [dictionary]
        Retorna la pizza con los ingredientes agregados en caso de que estos existiesen
    """
    new_pizza = pizza
    for ingrediente in ingredientes:
        new_pizza = add_ingrediente(new_pizza, ingrediente)
    return new_pizza