import sys

#Funcion para convertir segun tasa
def converter (money, key, dict):
    exchange_value = dict.get(key)
    return money * exchange_value

#Keys para las monedas
tasas_keys = ["Sol Peruano",
         "Peso Argentino",
         "Dolar Americano"]

#Argv
sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])

peso_chileno = float(sys.argv[4])

#Formacion del diccionario
tasas = dict([
    (tasas_keys[0], sol),
    (tasas_keys[1], peso_argentino),
    (tasas_keys[2], dolar)])

#Salida
print(f"Los {peso_chileno} pesos equivalen a:")
print(f"{converter(peso_chileno, tasas_keys[0], tasas):.1f} {tasas_keys[0]}")
print(f"{converter(peso_chileno, tasas_keys[1], tasas):.1f} {tasas_keys[1]}")
print(f"{converter(peso_chileno, tasas_keys[2], tasas):.1f} {tasas_keys[2]}")