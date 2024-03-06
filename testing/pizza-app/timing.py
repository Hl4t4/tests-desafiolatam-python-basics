def pizza_timing(pizza):
    """Esta funcion actualiza cuanto se demorara la entrega de la pizza
    Parameters
    ----------
    pizza: [dictionary]
        Pizza con masa, salsa, ingredientes y tiempo
    Returns
    ----------
    [dictionary]
        Retorna la pizza con el tiempo actualizado
    """
    new_pizza = pizza
    new_pizza['tiempo'] = sum([2 for ingrediente, value in new_pizza['ingredientes'].items() if value]) + 20
    return new_pizza