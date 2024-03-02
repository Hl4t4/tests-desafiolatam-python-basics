import argparse # Libreria usada para obtener argumentos del inicio de la aplicacion

ventas = {"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

if __name__ == "__main__":
    #Lectura de argumentos de ingreso
    parser = argparse.ArgumentParser(description="Filtro de diccionario por valor") # add description later
    parser.add_argument("mayor", type=int)
    args = parser.parse_args()

    mayor = args.mayor
    ventas_filtradas = ({mes:venta for mes,venta in ventas.items() if venta > mayor})
    print(ventas_filtradas)