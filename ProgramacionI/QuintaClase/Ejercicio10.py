
# Consigna
#  Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#       a. Todos los números impares desde 1 hasta ese número separados por comas.
#       b. La cuenta atrás desde ese número hasta cero separados por comas.
#       c. Que indique si es primo o no.
#       d. Por último, su factorial.

continuar_ejecucion = True                              

def numeros_impares(numero_ingresado):                  
    primer_iteracion = True                            
    for numero in range(1, numero_ingresado + 1):       
        if numero % 2 != 0:                             
            if primer_iteracion:                        
                primer_iteracion= False                 
                print(numero, end="")
            else:                                       
                print(", ", numero, end="")
    print()                                              

def cuenta_atras(numero_ingresado):                     
    primer_iteracion = True                             
    for numero in range(numero_ingresado, -1, -1):      
        if primer_iteracion:                            
            primer_iteracion= False                     
            print(numero, end="")
        else:                                           
            print(", ", numero, end="") 
    print()                                             

def indicar_numero_primo(numero_ingresado):            
    es_primo = True                                     
    if numero_ingresado < 2:                             
        es_primo = False                                
    for numero in range(2, int(numero_ingresado**0.5 + 1)): 
        if numero_ingresado % numero == 0:              
            es_primo = False                             
    if es_primo:                                         
        print(f"El número ingresado {numero_del_usuario} es primo")
    else:                                                
        print(f"El número ingresado {numero_del_usuario} no es primo")
    print()                                               
        
def factorial(numero_ingresado):                         
    valor_inicial = 1                                    
    for numero in range(2, numero_ingresado + 1):        
        valor_inicial *= numero                          
    print(f"El factorial del número {numero_del_usuario} es {valor_inicial}") 
    print()                                              

    
while continuar_ejecucion:                                             
    numero_del_usuario = int(input("Por favor, ingrese un número: \n"))

    print("------- Números impares -------\n")                          
    numeros_impares(numero_del_usuario)                                  
    print("------- Números al revés -------\n")                         
    cuenta_atras(numero_del_usuario)                                    
    print("------- Es primo -------\n")                                 
    es_primo = indicar_numero_primo(numero_del_usuario)                 
    print("------- Factorial -------\n")                                
    su_factorial = factorial(numero_del_usuario)                       
    
    desea_continuar = input("¿Desea continuar ejecutando el programa? (SI/NO) \n")   
                                                                                    
    if desea_continuar == "no":                                                     
        print("La ejecución del programa finalizó con éxito, muchas gracias")        
        exit()                                                                     
    elif desea_continuar == "si":                                                   
        continuar_ejecucion
    else:                                                                           
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()