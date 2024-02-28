from lib_desafio01 import input_number
from lib_desafio01 import utilidades

precio = input_number("Ingrese el precio de suscripcion del año anterior: $", float) 
numero_usuarios_normales = input_number("Ingrese la cantidad de usuarios normales del año anterior: ", int)
numero_usuarios_premium = input_number("Ingrese la cantidad de usuarios premium del año anterior: ", int)
gasto_total = input_number("Ingrese los gastos totales del año anterior: $", float) 
utilidades_anteriores = utilidades(precio, numero_usuarios_normales, numero_usuarios_premium, gasto_total)
print(f"Las utilidades del año anterior son: ${utilidades_anteriores:.2f}")

precio = input_number("Ingrese el precio de suscripcion de este año: $", float) 
numero_usuarios_normales = input_number("Ingrese la cantidad de usuarios normales de este año: ", int)
numero_usuarios_premium = input_number("Ingrese la cantidad de usuarios premium de este año: ", int)
gasto_total = input_number("Ingrese los gastos totales de este año: $", float) 
utilidades_actuales = utilidades(precio, numero_usuarios_normales, numero_usuarios_premium, gasto_total)
print(f"Las utilidades actuales son: ${utilidades_actuales:.2f}")

print(f"La razon entre las utilidades actuales y del año anterior es: {utilidades_actuales/utilidades_anteriores:.2f}")