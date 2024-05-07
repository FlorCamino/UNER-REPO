
# Consigna
# Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
# validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
# informarle que no se puede procesar el dato.

def es_vocal(letra):  
    print("---------------------------------")
    print("-------- Resultado Final --------")    
    if letra in "aeiou":
        print("Es vocal")
    else:
        print("No es vocal")
       
continuar_ejecucion = True                                                                          
while continuar_ejecucion:             

    letra_ingresada = input("Por favor, ingrese una letra: \n").lower()
    
    if len(letra_ingresada) == 1:
        es_vocal(letra_ingresada)  
    else:
        print("¡Error! Usted ha ingresado una cantidad no permitida de caracteres, fin de la ejecución")
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