
# Consigna

# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
# resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
# el grupo que le corresponde.


continuar_ejecucion = True                                                                          
while continuar_ejecucion:                                                                          
    alumno_nombre = input("Por favor, ingrese el nombre del alumno del curso: ").lower()           
    sexo_alumno = input("Por favor, ingrese el sexo del alumno del curso: (F/M)").lower()             
    primera_letra = alumno_nombre[0]                                                               
    def grupo_alumno(alumno,sexo, grupo):                                                           
        if sexo == "m":                                                                             
            print(f"El alumno '{alumno}' pertenece al grupo {grupo}")                               
        else:                                                                                       
            print(f"La alumna '{alumno}' pertenece al grupo {grupo}")                               
    
    if (primera_letra > 'n' and primera_letra <= 'z' and sexo_alumno == "m") or ( primera_letra >= 'a' and primera_letra < 'm' and sexo_alumno == "f"):
        grupo_alumno(alumno_nombre, sexo_alumno, "A")                           
    elif (primera_letra > 'a' and primera_letra <= 'n' and sexo_alumno == "m") or ( primera_letra >= 'm' and primera_letra <= 'z' and sexo_alumno == "f"): 
         grupo_alumno(alumno_nombre, sexo_alumno, "B")
    else:
        print("Fin de la ejecución, uno de los valores ingresados no corresponde")
        exit()

    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()    
                                                                                       
    if desea_continuar == "no":                                                         
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                     
        continuar_ejecucion
    else:                                                                             
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()