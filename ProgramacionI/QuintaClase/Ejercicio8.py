# Consigna
# Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

continuar_ejecucion = True                                          # Variable booleana con valor en true

while continuar_ejecucion:                                          # Se utiliza un While para ejecutar un programa hasta que el usuario desee finalizarlo
    edad_usuario = int(input("Por favor indiquenos su edad:  "))    # Se solicita el valor de la edad que se va a comparar y se lo castea a integer            
    if edad_usuario >= 18:                                          # Se utiliza la estructura if para evaluar la condición que es la edad de usuario comparador (mayor o igual) y el 18 que es la mayoria de años
        print("Es mayor de edad")                                   # Se imprime el valor en caso de que la condicion del if se cumpla 
    else:                                                           # Si no se cumple la condición ingresa en else e imprime el valor por defecto
        print("No es mayor de edad") 
    desea_continuar = input("¿Desea continuar con la ejecución? (SI/NO)\n").lower() # Almaceno en una variable el valo de la consulta del usuario si desea continuar y convertido a minúscula
    if desea_continuar == "no":                                                     # Comparo el valor ingresado por el usuario con la string negativa ya que el valor por defecto es true y 
        continuar_ejecucion = False                                                 # hasta que la condición no se convierta a falsa continuará siendo true, alli le cambio el valor a falso, 
        print("El programa ha finalizado, muchas gracias")                          # Finalmente muestro un mensaje de cierre del programa
    elif desea_continuar == "si":                                                   # Capturo las el valor donde la variable sea igual al strin "si" para impedir que se ejecute con valores inválidos
        continuar_ejecucion
    else:                                                                           # Si el valor no es ni "si" ni "no" entonces se ejecuta esta sentencia el cual finaliza la ejecución del programa y,
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  # Muestra un mensaje de error
        exit()
                          