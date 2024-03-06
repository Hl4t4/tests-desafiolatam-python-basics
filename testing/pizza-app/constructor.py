def pizza_constructor(ingredientes = {}):
    ingredientes_base = ({ingrediente:False for ingrediente in ingredientes})
    pizza = {"masa": "Masa Tradicional", "salsa": "Salsa de Tomate", "ingredientes": ingredientes_base, "tiempo": 20}
    return pizza
