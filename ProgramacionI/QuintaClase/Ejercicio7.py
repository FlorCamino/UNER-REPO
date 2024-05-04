# Consigna
# Que imprima todos los números entre el 100 y el 199.

numero = 100 + 1                    # Incicializacion de las variables numero desde el valor inicial + 1
contador = 0                        # Se inicializa la variable contador para contabilizar las iteraciones

while numero < 199:                 #Cabecera del bucle, se utiliza while ya que se conocen las veces a iterar
    print(str(numero).rjust(5), end=" ") # Se imprime la variable número casteado a string, además incopore esta 
                                         # función nativa de Python para imprimir los números justificados y un espacio al final del mismo
    numero += 1                          # Incremento de número
    contador += 1                        # Incremento de contador
    if contador == 10:                   # Se agrega una estructura if para que cuando se impriman un total de
        print("\n")                      # 10 se realice un salto de línea y se imprima debajo, tambien reinicie
        contador = 0                     # el valor de contador a 0