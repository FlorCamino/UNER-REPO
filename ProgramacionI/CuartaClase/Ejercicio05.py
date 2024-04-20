# Consigna

''' Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
forma: “La respuesta es XX” ''' 

# Solución

primer_numero = int(input("Por favor, ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
tercer_numero = int(input("Ahora, ingrese el tercer número: "))

resultado_final = (primer_numero + segundo_numero) 
resultado_final = resultado_final * tercer_numero

print("La respuesta es",resultado_final)