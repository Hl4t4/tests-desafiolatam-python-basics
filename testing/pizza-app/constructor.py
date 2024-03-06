def pizza_constructor(ingredientes = []):
    """Esta funcion genera la base de la pizza
    Parameters
    ----------
    ingredientes: [list]
        Lista de ingredientes disponibles en la tienda
    Returns
    ----------
    [dictionary]
        Retorna la pizza con los valores base de masa, salsa, ingrendientes y tiempo
    """
    ingredientes_base = ({ingrediente:False for ingrediente in ingredientes})
    pizza = {"masa": "Masa Tradicional", "salsa": "Salsa de Tomate", "ingredientes": ingredientes_base, "tiempo": 20}
    return pizza
