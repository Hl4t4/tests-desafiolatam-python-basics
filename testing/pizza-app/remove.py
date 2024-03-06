from timing import pizza_timing

def remove_ingrediente(pizza, ingrediente):
    """Esta funcion remueve un ingrediente de la pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    ingrediente: [str]
        Ingrediente que se quiere remover
    Returns
    ----------
    [dictionary]
        Retorna la pizza con el ingrediente removido en caso de que existiese
    """
    new_pizza = pizza
    if new_pizza['ingredientes'].get(ingrediente) != None:
        new_pizza['ingredientes'][ingrediente] = False
        new_pizza = pizza_timing(new_pizza)
    else:
        print(f"{ingrediente} es un ingrediente invalido")
    return new_pizza

def remove_ingredientes(pizza, ingredientes):
    """Esta funcion remueve un listado de ingredientes de la pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    ingredientes: [list]
        Listado de ingredientes a eliminar
    Returns
    ----------
    [dictionary]
        Retorna la pizza con los ingredientes removidos en caso de que estos existiesen
    """
    new_pizza = pizza
    for ingrediente in ingredientes:
        new_pizza = remove_ingrediente(new_pizza, ingrediente)
    return new_pizza
