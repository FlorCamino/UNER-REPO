# Consigna

'''  Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
día, mes y año. Ej:
Usuario ingresa: 17/05/1985
Programa imprime: Día: 17, Mes: 05 y Año: 1985 ''' 

# Solución

fechaIngresada = input("Por favor, ingrese una fecha con el siguiente formato (dd/mm/aaaa): ")

dia = fechaIngresada[0:2]
mes = fechaIngresada[3:5]
anio = fechaIngresada[6:11]

print(f"Día: {dia}, Mes: {mes} y Año: {anio}")