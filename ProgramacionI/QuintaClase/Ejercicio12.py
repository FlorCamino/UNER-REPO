
# Consigna 

# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

continuar_ejecucion = True                                                             
while continuar_ejecucion:                                                             
    dia_semana = input("Por favor, ingrese el nombre de un día de la semana: ").lower()
    
    match dia_semana:                                                                  
        case "lunes":
            print("Usted ha ingresado Lunes")                                          
        case "martes":
            print("Usted ha ingresado Martes")                                        
        case "miercoles" | "miércoles":
            print("Usted ha ingresado Miércoles")                                      
        case "jueves":
            print("Usted ha ingresado Jueves")                                         
        case "viernes":
            print("Usted ha ingresado Viernes")                                        
        case "sabado" | "sábado":
            print("Usted ha ingresado Sábado")                                         
        case "domingo":
            print("Usted ha ingresado Domingo")                                        
        case _:
            print("El valor que ingreso no corresponde a un día de la semana")         

    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()   
                                                                                       
    if desea_continuar == "no":                                                         
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                      
        continuar_ejecucion
    else:                                                                              
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()