efemerides = {'1 de Enero': 'Año Nuevo',
    '27 de Febrero': 'Terremoto en Chile',
    '8 de Marzo': 'Día de la Mujer',
    '21 de Mayo': 'Glorias Navales',
    '18 de Septiembre': 'Fiestas Patrias',
    '19 de Septiembre': 'Glorias del Ejercito',
    '25 de Diciembre': 'Navidad'}

efemerides = ({fecha.lower():efemeridad for fecha,efemeridad in efemerides.items()})
print(efemerides)

fecha = input('Ingrese la fecha por favor (Formato XX de Mes): ').lower()


# print(efemerides[fecha])

print(efemerides.get(fecha, "Fecha sin eventos"))