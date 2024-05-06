# Consigna
# Que imprima todos los números entre el 100 y el 199.

numero = 100 + 1                    
contador = 0                       

while numero < 199:                 
    print(str(numero).rjust(5), end=" ") 
                                         
    numero += 1                          
    contador += 1                        
    if contador == 10:                   
        print("\n")                      
        contador = 0                     