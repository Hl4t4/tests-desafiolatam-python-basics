import getpass

password = getpass.getpass("Ingrese la clave secreta: ")

while password != "valida":
    password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez.")
print("Clave Correcta. Puedes utilizar tu programa")