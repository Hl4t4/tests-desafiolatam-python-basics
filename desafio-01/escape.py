from lib_desafio01 import input_number

def velocidad_escape (r, g):
    return (2*g*r)**(1/2)

#Ciclo para preguntar por el radio
radio = input_number("Ingrese el radio r de la tierra [Km]: ", float)
radio = radio * 1000 # Debido a que la formula pide metros y la entrada es en kilometros 

#Ciclo para preguntar por la constante de gravedad
constante_gravedad = input_number("Ingrese la constante gratitacional g [m/s^2]: ", float)

print(f"La velocidad de escape Ve es: {velocidad_escape(radio, constante_gravedad):.1f} [m/s]")