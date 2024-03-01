from lib_desafio02 import input_number
import argparse

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

def imc_calculator (weight, height):
    return weight / (height/100)**2 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculadora IMC ingresar peso en Kg y altura en cm") # add description later
    parser.add_argument("weight", type=float)
    parser.add_argument("height", type=float)
    args = parser.parse_args()
    
    weight = args.weight
    height = args.height

    imc = imc_calculator(weight, height)
    imc_name = imc_calculator_index(imc)

    print(f'Su IMC es {imc:.2f}')
    print("La clasificacion OMS es " + imc_name)
