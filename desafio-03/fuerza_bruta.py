from string import ascii_lowercase
import getpass #Para passwords
import re # Para expresiones regulares
import timeit #Testing de tiempos, no necesario realmente

# Se inicia la expresion regular a usar y pide la contraseña, para luego hacer un match
pattern = re.compile("[a-z]+")
password = getpass.getpass("Ingrese la contraseña: ")
match = pattern.match(password)

# Se pide contraseña nueva hasta que se entrege una valida que sea solo letras sin contar la ñ
while (not match):
    password = getpass.getpass("Entrada no valida solo se aceptan letras mayusculas y minusculas. ").lower()
    match = pattern.match(password)


#Contar la posicion de la letra para saber cantidad de intentos 
difficulty = 0
for char in password:
    difficulty+= ord(char) - ord('a') + 1

print(f"La contraseña fue forzada en {difficulty} intentos")

# Usando for
difficulty = 0
for char in password:
    for ascii_char in ascii_lowercase:
        difficulty+= 1
        if char == ascii_char:
            break
print(f"La contraseña fue forzada en {difficulty} intentos")

# Usando comprehensions

difficulty = sum([sum([1 for ascii_char in ascii_lowercase if ascii_char <= char]) for char in password])
print(f"La contraseña fue forzada en {difficulty} intentos")


#############

#TESTING TIMES

#############

print("\n\nTesting times\n\n")

def test01():
    difficulty = 0
    for char in password:
        difficulty+= ord(char) - ord('a') + 1
    #print(f"La contraseña fue forzada en {difficulty} intentos")
print(f"Metodo que solo cuenta por la letra {timeit.timeit('test01()',setup='from __main__ import test01' , number=10000)}")

def test02():
    difficulty = 0
    for char in password:
        for ascii_char in ascii_lowercase:
            difficulty+= 1
            if char == ascii_char:
                break
    #print(f"La contraseña fue forzada en {difficulty} intentos")
print(f"Metodo usando for {timeit.timeit('test02()',setup='from __main__ import test02' , number=10000)}")

def test03():
    difficulty = sum([sum([1 for ascii_char in ascii_lowercase if ascii_char <= char]) for char in password])
    #print(f"La contraseña fue forzada en {difficulty} intentos")
print(f"Metodo usando comprehensions {timeit.timeit('test03()',setup='from __main__ import test03' , number=10000)}")