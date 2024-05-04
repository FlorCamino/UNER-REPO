
# Consigna 

# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

continuar_ejecucion = True                                                             # Se declara una variable para ejecutar el programa hasta que dicha variable se convierta en False o finalice el programa
while continuar_ejecucion:                                                             # Itera hasta que el continuar_ejecucion sea False
    dia_semana = input("Por favor, ingrese el nombre de un día de la semana: ").lower()# Variable que almacena el string del dia de la semana ingresado por el usuario 
    
    match dia_semana:                                                                  # La variable día de la semana es quién debera conincidir con algún valor case
        case "lunes":
            print("Usted ha ingresado Lunes")                                          # Si es lunes muestra el mensaje dentro del cuerpo de mismo y finaliza la ejecución
        case "martes":
            print("Usted ha ingresado Martes")                                         # Si no es lunes evalua que coincida con martes, y muestra el mensaje en caso de que sea igual y finaliza
        case "miercoles" | "miércoles":
            print("Usted ha ingresado Miércoles")                                      # Si no es lunes ni martes evalúa la condición de miercoles y miércoles y si coincide muestra el mensaje
        case "jueves":
            print("Usted ha ingresado Jueves")                                         # Si no es ninguna de las anteriores evalua el contra jueves y si coincide muestra el mensaje y finaliza
        case "viernes":
            print("Usted ha ingresado Viernes")                                        # Si no es ninguna de las anteriores evalua el contra viernes y si coincide muestra el mensaje y finaliza
        case "sabado" | "sábado":
            print("Usted ha ingresado Sábado")                                         # Si no es ninguna de las anteriores evalua el contra sabado / sábado y si coincide muestra el mensaje y finaliza
        case "domingo":
            print("Usted ha ingresado Domingo")                                        # Si no es ninguna de las anteriores evalua el contra domingo y si coincide muestra el mensaje y finaliza
        case _:
            print("El valor que ingreso no corresponde a un día de la semana")         # Si no es ninguna de las anteriores muestra el mensaje por defecto y finaliza

    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()   # Se consulta al usuario si desea continuar con la ejecución del programa, 
                                                                                       # se convierte el valor ingresado a minúscula y se almacena en una variable
    if desea_continuar == "no":                                                        # Se compara el valor ingresado por el usuario con la string "no" en minúsculas 
        print("¡El programa ha finalizado, muchas gracias!")                           # Se muestra un mensaje por consola
        exit()                                                                         # Se cierra la ejecucón del programa
    elif desea_continuar == "si":                                                      # Capturo las el valor donde la variable sea igual al strin "si" para impedir que se ejecute con valores inválidos
        continuar_ejecucion
    else:                                                                              # Si el valor no es ni "si" ni "no" entonces se ejecuta esta sentencia el cual finaliza la ejecución del programa y,
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  # Muestra un mensaje de error
        exit()