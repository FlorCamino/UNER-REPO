
# Consigna 

# Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
# encuentran en dicha frase.
continuar_ejecucion = True                                            # Se declara una variable para ejecutar el programa hasta que dicha variable se convierta en False o finalice el programa
while continuar_ejecucion:                                            # Itera hasta que el continuar_ejecucion sea False
    frase_ingresada = input("Por favor, ingrese una frase: ").lower() # Solicito al usuario ingresar una frase y la asigno a una variable
    contador = 0                                                      # Declaro una variable contador en 0

    for letra in frase_ingresada:                                     # Itero sobre cada letra de la frase que ingreo el usuario 
        if letra in "aeiou":                                          # Evaluo que la letra de cada iteraciín se encuentre en la string "aeiou"
            contador += 1                                             # Incremento la variable contador en 1
    print(f"La frase '{frase_ingresada}' contiene un total de {contador} vocales")     # Muestro el resultado por la consola
    
    desea_continuar = input("¿Desea continuar comparando números? (SI/NO) ").lower()   # Se consulta al usuario si desea continuar con la ejecución del programa, 
                                                                                       # se convierte el valor ingresado a minúscula y se almacena en una variable
    if desea_continuar == "no":                                                        # Se compara el valor ingresado por el usuario con la string "no" en minúsculas 
        print("¡El programa ha finalizado, muchas gracias!")                           # Se muestra un mensaje por consola
        exit()                                                                         # Se cierra la ejecucón del programa
    elif desea_continuar == "si":                                                      # Capturo las el valor donde la variable sea igual al strin "si" para impedir que se ejecute con valores inválidos
        continuar_ejecucion
    else:                                                                              # Si el valor no es ni "si" ni "no" entonces se ejecuta esta sentencia el cual finaliza la ejecución del programa y,
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  # Muestra un mensaje de error
        exit()