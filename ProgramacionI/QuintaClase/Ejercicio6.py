# Consigna
#  Que pida al usuario una palabra y la muestre por pantalla 10 veces
numero = 0                                                           # Inicialización 
palabra_ingresada = input("Por favor ingrese una palabra: ")         # Solicitud del valor por única vez
while numero < 10:                                                   # Cabecera del bucle (como se conoce las veces que debe iterar se utiza el bucle while)
    print(f"{palabra_ingresada} \n")                                 # Se imprime el valor de la palabra dentro del bucle junto al salto de línea
    numero += 1                                                      # Incremento del valor de número en 1