def pizza_timing(pizza):
    new_pizza = pizza
    new_pizza['tiempo'] = sum([2 for ingrediente, value in new_pizza['ingredientes'].items() if value]) + 20
    return new_pizza