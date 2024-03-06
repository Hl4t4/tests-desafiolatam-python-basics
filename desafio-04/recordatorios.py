recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# add ['2021-02-02', "06:00", "Empezar el Año"] Dice 2 de febrero pero usare de enero
recordatorios.insert(1, ['2021-01-02', "06:00", "Empezar el Año"])
# Change ['2021-07-15', "13:00", "No hacer nada es feriado"] a ['2021-07-16', "13:00", "No hacer nada es feriado"]
recordatorios[3] = ['2021-07-16', "13:00", "No hacer nada es feriado"]
# del ['2021-05-01', "15:00", "No trabajar"]
del recordatorios[2]
# add ['2021-12-24', "22:00", "Cena de Navidad"]
recordatorios.insert(-1, ['2021-12-24', "22:00", "Cena de Navidad"])
# add ['2021-12-31', "22:00", "Cena de Año Nuevo"]
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])


# Output
print(recordatorios)
