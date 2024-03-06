#Filtrado

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
# print(filtered_array)

result1 = [numero for numero in a if numero >= 1000]
print(result1)

#Adicto a redes

tiempo_redes = [120, 50, 600, 30, 90, 10, 200, 0, 500]
result2 = ["bien" if tiempo < 90 else "mal" for tiempo in tiempo_redes]
print(result2)

#Segundos a minutos

seconds = [100, 50, 1000, 5000, 1000, 500]
result3 = [int(second/60) for second in seconds]
print(result3)

#Paises

paises = ["Mexico", "Chile", "Argentina", "Peru"]
usuarios= [70, 50, 55, 80]
result4 = ({pais:usuario for pais,usuario in zip(paises,usuarios) if usuario < 60})
print(result4)

#Ventas

meses = ["Octubre", "Noviembre", "Diciembre"]
ventas = [65000, 68000, 72000]
result5 = ({mes:venta*1.1 for mes,venta in zip(meses, ventas)})
result6 = ({mes:venta*0.8 for mes,venta in zip(meses, ventas)})

print(result5)
print(result6)