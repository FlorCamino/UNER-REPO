
# Consigna 

# Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

def retornar_dia_semana(dia_ingresado):
    print("---------------------------------")
    print("-------- Resultado Final --------") 
    match dia_ingresado:                                                                  
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

continuar_ejecucion = True                                                             
while continuar_ejecucion:                                                             
    dia_semana = input("Por favor, ingrese el nombre de un día de la semana: ").lower()
    
    if dia_semana.strip() != "":
        retornar_dia_semana(dia_semana)
    else:
        print("Debe ingresar un dia de la semana, por favor, vuelta a intentarlo.")        

    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()   
                                                                                       
    if desea_continuar == "no":                                                         
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                      
        continuar_ejecucion
    else:                                                                              
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()