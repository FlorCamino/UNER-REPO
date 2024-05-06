
# Consigna
# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
# en que ambos números son iguales

continuar_ejecucion = True                                                  

def comparar_numeros(primer_numero, segundo_numero):                        
    if primer_numero > segundo_numero:                                     
        print(f"El número {primer_numero} es mayor que {segundo_numero}")   
    elif primer_numero < segundo_numero:                                    
        print(f"El número {segundo_numero} es mayor que {primer_numero}")   
    else:                                                                   
        print(f"Los números ingresados son iguales")                        
        
                                            
while continuar_ejecucion:                                                  
    primer_numero = int(input("Por favor, ingrese el primer número: "))    
    segundo_numero = int(input("Por favor, ingrese el segundo número: "))
    comparar_numeros(primer_numero, segundo_numero)                         
    desea_continuar = input("¿Desea continuar comparando números? (SI/NO) ").lower() 
    if desea_continuar == "no":                                             
        continuar_ejecucion = False                                         
        print("¡El programa ha finalizado, muchas gracias!")                
    elif desea_continuar == "si":                                           
        continuar_ejecucion
    else:                                                                   
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()