#Funcion que calcula la media
def media(values):
    return sum(values)/len(values)

#Funcion que filtra los valores que estan sobre la media devolvindo sus posiciones en el arreglo de entrada
def sobre_media(values):
    media_value = media(values)
    return [index for index, value in enumerate(values) if value > media_value]

#Prueba
velocidades = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

posiciones = sobre_media(velocidades)

print(posiciones)