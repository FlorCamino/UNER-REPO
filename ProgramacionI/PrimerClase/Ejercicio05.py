# Consigna

''' Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
forma: “La respuesta es XX” ''' 

# Solución


primerNumero = int(input("Por favor, ingrese el primer número: "))
segundoNumero = int(input("Ingrese el segundo número: "))
tercerNumero = int(input("Ahora, ingrese el tercer número: "))

resultadoFinal = (primerNumero + segundoNumero) * tercerNumero

print(f"La respuesta es {resultadoFinal}")