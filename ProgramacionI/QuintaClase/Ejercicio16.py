# Consigna
# Que imprima elsiguiente patrón:
#       5 4 3 2 1
#       4 3 2 1
#       3 2 1
#       2 1
#       1
        
def  imprimir_patron(numero_ingresado):
    print("----------------------------")
    print("------- Patrón final -------")
    for inicio in range(numero_ingresado, 0, -1): 
        for resto in range(inicio, 0, -1):
            print(resto, end=" ")  # Imprime la línea hasta el final desde el numero de inicio
        print()
        
continuar_ejecucion = True                                                                          
while continuar_ejecucion:             

    NUMERO_INGRESADO = 5
    
    imprimir_patron(NUMERO_INGRESADO)   

    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()    
                                                                                       
    if desea_continuar == "no":                                                         
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                     
        continuar_ejecucion
    else:                                                                             
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()