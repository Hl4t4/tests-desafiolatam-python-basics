import sys

#Funcion principal que al recibir un diccionario, lo filtra segun el umbral recibido y en la direccion buscada
def filtro(diccionario, umbral, mayor = True):
    diccionario_filtrado = {}
    if mayor:
        diccionario_filtrado = ({key:value for key,value in diccionario.items() if value > umbral})
        print("Los productos mayores al umbral son: ", ", ".join(list(diccionario_filtrado.keys())))
    else:
        diccionario_filtrado = ({key:value for key,value in diccionario.items() if value < umbral})
        print("Los productos menores al umbral son: ", ", ".join(list(diccionario_filtrado.keys())))
    return diccionario_filtrado

#Datos de ejemplo
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

precios_filtrados = None
umbral = int(sys.argv[1])
if len(sys.argv) >= 3: #Caso en el que hayan al menos 2 argumentos, se permiten mas argumentos pero no se usan
    mayor = sys.argv[2].lower()

if len(sys.argv) == 2: #Caso en el que hay solo 1 argumento, el umbral
    precios_filtrados = filtro(precios, umbral)
else:
    if mayor == 'menor':
        precios_filtrados = filtro(precios, umbral, mayor = False)
    elif mayor == 'mayor':
        precios_filtrados = filtro(precios, umbral, mayor = True)
    else:
        print("Lo sentimos, no es una operacion valida")