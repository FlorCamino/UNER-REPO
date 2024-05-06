

# Consigna
# Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
# múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
# ejemplos de posiblesrespuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
# no es bisiesto.

continuar_ejecucion = True                                                                          
while continuar_ejecucion:             
                                                                 
    anio_ingresado = int(input("Por favor, ingrese un año: \n"))
    
    def calcular_anio_bisiesto(anio_ingresado):
        es_bisiesto = False
        if  (anio_ingresado % 4 == 0 and anio_ingresado % 100 != 0)  or anio_ingresado % 400 == 0:
            es_bisiesto = True
        return es_bisiesto

    es_anio_bisiesto = calcular_anio_bisiesto(anio_ingresado)
    if es_anio_bisiesto:
        print(f"El año {anio_ingresado} es bisiesto")
    else:
        print(f"El año {anio_ingresado} NO es bisiesto")
        
    desea_continuar = input("¿Desea continuar ingresando valores? (SI/NO) ").lower()    
                                                                                       
    if desea_continuar == "no":                                                         
        print("¡El programa ha finalizado, muchas gracias!")                           
        exit()                                                                         
    elif desea_continuar == "si":                                                     
        continuar_ejecucion
    else:                                                                             
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()