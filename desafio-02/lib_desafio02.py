#Funcion para recibir un numero como int o float
#Recibe como parametros primero el texto a usar en el input y segundo el tipo de dato, si es float o int

def input_number (input_text, data_type):
    new_data = None
    if (data_type == int):
        while (not isinstance(new_data, int)):  
            try:
                new_data = int(input(input_text))
            except:
                print("Por favor ingresar un numero valido")
    elif (data_type == float):
        while (not isinstance(new_data, float)):  
            try:
                new_data = float(input(input_text))
            except:
                print("Por favor ingresar un numero valido")
    return new_data

#Funcion de calculo para emprendedores
def utilidades (p, u, un, gt):
    return p*u + 1.5*p*un - gt