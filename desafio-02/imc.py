import argparse # Libreria usada para obtener argumentos del inicio de la aplicacion

# Calcula segun el indice en que categoria queda
def imc_calculator_index (imc):
    match imc:
        case float(x) if x < 18.5:
            return "Bajo Peso"
        case float(x) if x >= 18.5 and x < 25:
            return "Adecuado"
        case float(x) if x >= 25 and x < 30:
            return "Sobrepeso"
        case float(x) if x >= 30 and x < 35:
            return "Obesidad Grado I"
        case float(x) if x >= 35 and x < 40:
            return "Obesidad Grado II"
        case float(x) if x >= 40:
            return "Obesidad Grado III"
        case _:
            return "Valor imc no valido"

# Calculo del imc
def imc_calculator (weight, height):
    return weight / (height/100)**2 

if __name__ == "__main__":
    #Obtencion de argumentos, que deben ser 2
    parser = argparse.ArgumentParser(description="Calculadora IMC ingresar peso en Kg y altura en cm") # add description later
    parser.add_argument("weight", type=float)
    parser.add_argument("height", type=float)
    args = parser.parse_args()
    
    weight = args.weight
    height = args.height

    #Calculo del imc y en que categoria queda
    imc = imc_calculator(weight, height)
    imc_name = imc_calculator_index(imc)

    #Impresion de los resultados
    print(f'Su IMC es {imc:.2f}')
    print("La clasificacion OMS es " + imc_name)
