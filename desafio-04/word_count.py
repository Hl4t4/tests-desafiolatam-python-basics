import sys

#Lectura del archivo
with open(sys.argv[1], "r") as file:
    texto=file.read()

#Se aprovecha la unicidad de elementos de set
unique_char = set(texto)
words = texto.split(" ")
unique_words = set(words)

#Se imprimen resultados
print(f"El número de caracteres distintos es: {len(unique_char)}")
print(f"El número de palabras distintas es: {len(unique_words)}")