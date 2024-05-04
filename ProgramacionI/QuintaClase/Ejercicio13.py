
# Consigna

# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
# resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
# el grupo que le corresponde.


continuar_ejecucion = True                                                                  # Se declara una variable para ejecutar el programa hasta que dicha variable se convierta en False o finalice el programa
while continuar_ejecucion:                                                                  # Itera hasta que el continuar_ejecucion sea False
    alumno_nombre = input("Por favor, ingrese el nombre del alumno del curso: ").lower()    # Variable que almacena el string del nombre del alumno 
    sexo_alumno = input("Por favor, ingrese el sexo del alumno del curso: (F/M)").lower()   # Variable que almacena el string del sexo del alumno   
    primera_letra = alumno_nombre[0]                                                        # Se declara la variable primera_letra con el valor del subindice 0 del del nombre del alumno
    def grupo_alumno(alumno,sexo, grupo):                                                   # Cabecera de la función que recibe como parámetros el nombre del alumno, su sexo y el grupo al cual pertenece
        if sexo == "m":                                                                     # Este if evalua que el sexo sea igual a masculino y, 
            print(f"El alumno '{alumno}' pertenece al grupo {grupo}")                       # retorna el mensaje utilizando los parámetros para mostrar el grupo
        else:                                                                               # Cuando el sexo sea femenino se ingresará al flujo del else
            print(f"La alumna '{alumno}' pertenece al grupo {grupo}")                       # retornando el mensaje para dicho flujo y el grupo al que pertenecen
    # IF : Se pregunta si la primer letra del nombre es mayor a n y menor o igual a Z y además su sexo es masculino, o, si es femenino y la primera letra es mayor o igual a y menor a m
    # Si la condición se cumple invoca la función grupo alumno y se envian como argumento el nombre, sexo y grupo el que pertenece
    # ELSE : Cuando la primera condición es falsa se evalúa la segunda condición donde si es masculino y su primer letra del nombre es mayor que a y menor igual que n o, si es femenino y
    # la primera letra del nombre es mayor o igual que m y menor o igual que z
    # En ese caso se invoca la función y se manda como argumento el nombre del alumno, sexo y grupo
    # Dentro del else se ejecuta un mensaje de error para los casos en que los valores ingresados no coincidan con los permitidos y finaliza la ejecución
    if (primera_letra > 'n' and primera_letra <= 'z' and sexo_alumno == "m") or ( primera_letra >= 'a' and primera_letra < 'm' and sexo_alumno == "f"):
        grupo_alumno(alumno_nombre, sexo_alumno, "A")                           
    elif (primera_letra > 'a' and primera_letra <= 'n' and sexo_alumno == "m") or ( primera_letra >= 'm' and primera_letra <= 'z' and sexo_alumno == "f"): 
         grupo_alumno(alumno_nombre, sexo_alumno, "B")
    else:
        print("Fin de la ejecución, uno de los valores ingresados no corresponde")
        exit()

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