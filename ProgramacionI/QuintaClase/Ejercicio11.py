
# Consigna 
# Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
# encuentran en dicha frase.

continuar_ejecucion = True                                            
while continuar_ejecucion:                                            
    frase_ingresada = input("Por favor, ingrese una frase: ").lower() 
    contador = 0                                                      

    for letra in frase_ingresada:                                      
        if letra in "aeiou":                                          
            contador += 1                                             
    print(f"La frase '{frase_ingresada}' contiene un total de {contador} vocales")     
    
    desea_continuar = input("¿Desea continuar comparando números? (SI/NO) ").lower()   
                                                                                       
    if desea_continuar == "no":                                                       
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                      
        continuar_ejecucion
    else:                                                                              
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()