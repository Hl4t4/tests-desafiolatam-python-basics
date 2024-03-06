import random

pool = [n for n in range(1,42)]

posiciones = ['primer número', 
              'segundo número', 
              'tercer número', 
              'cuarto número', 
              'quinto número', 
              'sexto número', 
              'comodín']

def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')

for posicion in posiciones:
    sacar_numero(posicion)
    # Opcional
    print(pool) # número ha sido eliminado

print("Sorteo ha finalizado")