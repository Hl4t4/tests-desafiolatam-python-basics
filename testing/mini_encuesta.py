def imprimir_encuesta(pregunta):
    print(preguntas)
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')
    return input('> ')

preguntas = ["Le agrada la ciudad donde nacio?",
             "Queria a su primera mascota?",
             "Le gusta su nombre?"]

respuestas = []

for pregunta in preguntas:
    respuestas.append(imprimir_encuesta(pregunta))

for respuesta in respuestas:
    print(f'La respuesta a la pregunta 1 fue {respuesta}')
print('Muchas gracias por responder la encuesta')
