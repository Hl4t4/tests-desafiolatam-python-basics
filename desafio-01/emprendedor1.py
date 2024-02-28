from lib_desafio01 import input_number
from lib_desafio01 import utilidades

precio = input_number("Ingrese el precio de suscripcion: $", float) 
numero_usuarios = input_number("Ingrese la cantidad de usuarios: ", int)
gasto_total = input_number("Ingrese los gastos totales: $", float)
utilidades_actuales = utilidades(precio, numero_usuarios, 0, gasto_total)

print(f"Las utilidades esperadas son: ${utilidades_actuales:.2f}")

