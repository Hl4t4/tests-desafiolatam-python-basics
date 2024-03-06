def factorial(n):
    if n <= 1: # Se entiende que deberia ser hasta 1, pero esto abarca tambien errores asi
        return 1
    else:
        return factorial(n-1)*n

def productoria(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista.pop()*productoria(lista)

def calcular (**kargs):
    for key, value in kargs.items():
        if 'fact_' in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif 'prod_' in key:
            print(f"La productoria de {value} es {productoria(value)}")
        else:
            print(f"El argumento {key} no es valido")

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

# lista = [4, 6, 7, 4, 3]

# print(lista[0])
# print(productoria(lista))