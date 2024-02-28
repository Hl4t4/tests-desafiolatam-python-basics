name = input("Cual es tu nombre?: ")
age = input("Coloque edad actual?: ")
job = input("Cual es tu empleo actual?: ")
company = input("Donde trabaja?: ")
description = input("Breve descripcion de aptitudes: ")
hobby = input("Cual es su pasatiempo?: ")
future = input("Que quiere a futuro?: ")
# text = f"Mi nombre es Bill, tengo {age} años y me desempeño como CEO en Microsoft. \nSoy Creativo, Apasionado y Visionario. \nMi pasatiempo es jugar Golf y me gustaría poder jubilarme pronto."
text = f"Mi nombre es {name}, tengo {age} años y me desempeño como {job} en {company}. \nSoy {description}. \nMi pasatiempo es {hobby} y me gustaría poder {future}."
print(text)