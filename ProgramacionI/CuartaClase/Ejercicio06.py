# Consigna

''' Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
número de comensales y mostrar cuánto debe pagar cada persona ''' 

# Solución

precio_total_cuenta = float(input("Por favor, ingrese el monto total de la cuenta: "))
cantidad_comensales = int(input("Ahora, indique la cantidad de comensales: "))

precio_por_persona = precio_total_cuenta / cantidad_comensales

print("Cada comensal deberá pagar el monto de $", precio_por_persona)