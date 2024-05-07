# Consigna
# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

continuar_ejecucion = True                                         
def calcular_mayoria_edad(edad):
    print("---------------------------------")
    print("-------- Resultado Final --------")                                         
    if edad >= 18:                                          
        print("Es mayor de edad")                                  
    else:                                                          
        print("No es mayor de edad")
  
while continuar_ejecucion:
    edad_ingresada = int(input("Por favor indiquenos su edad: \n"))
    if edad_ingresada > 0:
        calcular_mayoria_edad(edad_ingresada)
    else:
        print("El número ingresado es incorrecto, vuelta a intentarlo") 
    desea_continuar = input("¿Desea continuar con la ejecución? (SI/NO)\n").lower() 
    if desea_continuar == "no":                                                      
        continuar_ejecucion = False                                                  
        print("El programa ha finalizado, muchas gracias")                          
    elif desea_continuar == "si":                                                 
        continuar_ejecucion
    else:                                                                           
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()
                          