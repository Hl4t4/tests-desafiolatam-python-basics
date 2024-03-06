def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if p_level <= 3 and n_pregunta <= p_level*3: # se puede liberar la segunda condicion para que cualquier numero alto sea elegir nivel avanzado
        n_level = n_pregunta/p_level
        if n_level <= 1:
            level = "basicas"
        elif n_level <= 2:
            level = "intermedias"
        else:
            level = "avanzadas"
    else:
        level = "avanzadas"
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias