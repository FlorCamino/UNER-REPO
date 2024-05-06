# Consigna
# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

continuar_ejecucion = True                                         

while continuar_ejecucion:                                          
    edad_usuario = int(input("Por favor indiquenos su edad:  "))        
    if edad_usuario >= 18:                                          
        print("Es mayor de edad")                                  
    else:                                                          
        print("No es mayor de edad") 
    desea_continuar = input("¿Desea continuar con la ejecución? (SI/NO)\n").lower() 
    if desea_continuar == "no":                                                      
        continuar_ejecucion = False                                                  
        print("El programa ha finalizado, muchas gracias")                          
    elif desea_continuar == "si":                                                 
        continuar_ejecucion
    else:                                                                           
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()
                          