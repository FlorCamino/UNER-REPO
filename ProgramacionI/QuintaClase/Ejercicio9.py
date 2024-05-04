
# Consigna
# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
# en que ambos números son iguales
continuar_ejecucion = True                                                  # Se declara una variable para ejecutar el programa hasta que dicha variable se convierta en False

def comparar_numeros(primer_numero, segundo_numero):                        # Se utiliza una función que compara dos parámetros ingresados por el usuario retornando cual es mayo si es igual
    if primer_numero > segundo_numero:                                      # Cabecera de la estructura if que compara el primer numero mayor que el segundo  
        print(f"El número {primer_numero} es mayor que {segundo_numero}")   # Imprime por pantalla que el primer valor del segundo
    elif primer_numero < segundo_numero:                                    # Compara si el primero es menor que el segundo
        print(f"El número {segundo_numero} es mayor que {primer_numero}")   # Imprime el segundo valor como mayor al primero 
    else:                                                                   # Todo aquello que no cumpla la condición del if y elif ingresara en else o valor por defecto
        print(f"Los números ingresados son iguales")                        # En este caso los valores seran iguales lo cual retorna un mensaje
        
                                            
while continuar_ejecucion:                                                  # Se utiliza un bucle while para evaluar que la variable siempre sea True y sino ya no se ejecutará
    primer_numero = int(input("Por favor, ingrese el primer número: "))     # Solicitud de los números al usuario y se almacenan cada una en una variable
    segundo_numero = int(input("Por favor, ingrese el segundo número: "))
    comparar_numeros(primer_numero, segundo_numero)                         # Se invoca la función y se pasan las variables que ingreso el usuario
    desea_continuar = input("¿Desea continuar comparando números? (SI/NO) ").lower() # Se consulta al usuario si desea continuar con la ejecución del programa, se convierte el valor a minúscula
    if desea_continuar == "no":                                             # Se compara el valor ingresado por el usuario con el valo no en minúsculas
        continuar_ejecucion = False                                         # Se modifica el valor de continuar_ejecución en False
        print("¡El programa ha finalizado, muchas gracias!")                # Se muestra un mensaje de cierre y finaliza el programa
    elif desea_continuar == "si":                                           # Capturo las el valor donde la variable sea igual al strin "si" para impedir que se ejecute con valores inválidos
        continuar_ejecucion
    else:                                                                   # Si el valor no es ni "si" ni "no" entonces se ejecuta esta sentencia el cual finaliza la ejecución del programa y,
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  # Muestra un mensaje de error
        exit()