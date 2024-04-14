# Consigna

''' Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
número de comensales y mostrar cuánto debe pagar cada persona ''' 

# Solución

precioTotalCuenta = float(input("Por favor, ingrese el monto total de la cuenta: "))
cantidadComensales = int(input("Ahora, indique la cantidad de comensales: "))

precioPorPersona = precioTotalCuenta / cantidadComensales

print(f"Cada comensal deberá pagar el monto de ${precioPorPersona:.2f}")