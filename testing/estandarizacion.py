def media(values):
    return sum(values)/len(values)
def desviacion_estandar(values, media):
    n = len(values)
    sumatoria = 0
    for value in values:
        sumatoria += ((value - media)**2)
    return (sumatoria/(n-1))**0.5

def vector_normalizado(values):
    media_x = media(values)
    desviacion = desviacion_estandar(values, media_x)
    v_estandarizado = [(value-media_x)/desviacion for value in values]
    return media_x, desviacion, v_estandarizado

lista = [1, 2, 3, 4, 5]

media_x, desviacion, vector = vector_normalizado(lista)

print("La media es: ", media_x)
print("La Desviacion estandar es: ", desviacion)
print("La lista estandarizada es: ", vector)