
# Consigna 
# Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
# encuentran en dicha frase.

    
def contar_vocales(frase):
    contador = 0                                                      
    for letra in frase:                                      
        if letra in "aeiouáéíóú":                                          
            contador += 1  
    print("---------------------------------")
    print("-------- Resultado Final --------")                                           
    print(f"La frase '{frase}' contiene un total de {contador} vocales")   


continuar_ejecucion = True                                            
while continuar_ejecucion:                                            
    frase_ingresada = input("Por favor, ingrese una frase: ").lower() 
    
    if frase_ingresada.strip() != "":
        contar_vocales(frase_ingresada) 
    else:
        print("El campo no puede ser nulo, por favor, vuelva a intentarlo.")
    
    desea_continuar = input("¿Desea continuar comparando números? (SI/NO) ").lower()   
                                                                                       
    if desea_continuar == "no":                                                       
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                      
        continuar_ejecucion
    else:                                                                              
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()