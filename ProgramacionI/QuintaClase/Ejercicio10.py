
# Consigna
#  Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#       a. Todos los números impares desde 1 hasta ese número separados por comas.
#       b. La cuenta atrás desde ese número hasta cero separados por comas.
#       c. Que indique si es primo o no.
#       d. Por último, su factorial.

continuar_ejecucion = True                              # Se declara la variable con valor booleano true para ejecutar el programa

def numeros_impares(numero_ingresado):                  # Cabecera de la función con el número recibido como parámetro 
    primer_iteracion = True                             # Se declara una variable para saber si es la primer iteración del for
    for numero in range(1, numero_ingresado + 1):       # Cabecera del bucle for donde se recorre desde 1 hasta el valor de número con un incremento en 1 y asinando a variable número
        if numero % 2 != 0:                             # Divido el número que retorna cada iteración y realizo el modulo del valor por 2 y si el mismo es distinto a cero (no es par)
            if primer_iteracion:                        # Primer iteración siempre va a ser verdadero por lo que la condición se cumplirá en la primer iteración y alli le modificamos el valor, 
                primer_iteracion= False                 # También se imprime el numero y luego un espacio
                print(numero, end="")
            else:                                       # Cuando ya no es primera iteración ingresa en else e imprime una coma con espacio, el nuevo número y un espacio al final
                print(", ", numero, end="")
    print()                                             # Salto de línea visual para la consola 

def cuenta_atras(numero_ingresado):                     # Cabecera de la función con el número recibido como parámetro 
    primer_iteracion = True                             # Se declara una variable para saber si es la primer iteración del for
    for numero in range(numero_ingresado, -1, -1):      # Cabecera del bucle for donde se recorre desde el valor de número hasta el número previo a -1 y decrementando en 1
        if primer_iteracion:                            # Primer iteración siempre va a ser verdadero por lo que la condición se cumplirá en la primer iteración y alli le modificamos el valor, 
            primer_iteracion= False                     # También se imprime el numero y luego un espacio
            print(numero, end="")
        else:                                           # Cuando ya no es primera iteración ingresa en else e imprime una coma con espacio, el nuevo número y un espacio al final
            print(", ", numero, end="") 
    print()                                             # Salto de línea visual para la consola 

def indicar_numero_primo(numero_ingresado):             # Cabecera de la función con el número recibido como parámetro  
    es_primo = True                                     # El valor inicial de la variable es_primo es true
    if numero_ingresado < 2:                            # Verifico si el número ingresado es menor a 2 y le asigno es_primo=Falso 
        es_primo = False                                # (el número 1 no es primo por lo que capturamos su valor y retornamos falso sin iterar)
    for numero in range(2, int(numero_ingresado**0.5 + 1)): # Cabecera del bucle for donde se recorre desde el número 2 hasta la raíz cuadrada del número ingresado (inclusive), incrementando en 1 en cada paso.
        if numero_ingresado % numero == 0:               # En este caso se realiza el módulo entre el numero ingresado por el usuario y el resultado por iteración de la variable número y se compara con cero 
            es_primo = False                             # Cuando el número que ingresa el usuario modulo 2 es igual o entonces no es un número primo por lo que la variable es_primo se le asigna el valor False
    if es_primo:                                         # Este condicional evalúa que es_primo sea true y retorna el mensaje por consola
        print(f"El número ingresado {numero_del_usuario} es primo")
    else:                                                # Si la variable es_primo tiene el valor False entonces se imprime el body que se encuentra dentro del else
        print(f"El número ingresado {numero_del_usuario} no es primo")
    print()                                              # Salto de línea visual para la consola 
        
def factorial(numero_ingresado):                         # Cabecera de la función con el número recibido como parámetro  
    valor_inicial = 1                                    # Para acumular el el valor del factorial, se declara una variable en 1 
    for numero in range(2, numero_ingresado + 1):        # Cabecera del bucle for donde se recorre desde el número 2 hasta el número ingresado, incrementando en 1 este valor en cada iteración se asigna a la variable número.
        valor_inicial *= numero                          # Número que obtiene el valor por cada iteración se multiplicara a valor inicial quien acumulara la multiplicacion de todos los números 
    print(f"El factorial del número {numero_del_usuario} es {valor_inicial}") # Se imprime por consola el valor final del factorial
    print()                                              # Salto de línea visual para la consola 

    
while continuar_ejecucion:                                              # Este bucle representa la iteración de un programa hasta que continuar_ejecución se convierta en False
    numero_del_usuario = int(input("Por favor, ingrese un número: \n")) # Número_del_usuario es el valor ingresado por el usuario que luego se castea a string

    print("------- Números impares -------\n")                          # Mensaje visual para identificar el resultado en la consola de los números impares
    numeros_impares(numero_del_usuario)                                 # Se invoca a la fucnion numeros_impares donde se le pasa como argumento el numero que ingreso el usuario 
    print("------- Números al revés -------\n")                         # Mensaje visual para identificar el resultado en la consola de los números de manera inversa
    cuenta_atras(numero_del_usuario)                                    # Se invoca a la función cuenta_atras donde se le pasa como argumento el numero que ingreso el usuario 
    print("------- Es primo -------\n")                                 # Mensaje visual para identificar el resultado en la consola del resultado de número primo
    es_primo = indicar_numero_primo(numero_del_usuario)                 # Se invoca a la función indicar_numero_primo donde se le pasa como argumento el numero que ingreso el usuario
    print("------- Factorial -------\n")                                # Mensaje visual para identificar el resultado en la consola del resultado del factorial
    su_factorial = factorial(numero_del_usuario)                        # Se invoca a la función factorial donde se le pasa como argumento el numero que ingreso el usuario
    
    desea_continuar = input("¿Desea continuar ejecutando el programa? (SI/NO) \n")  # Se consulta al usuario si desea continuar con la ejecución debe escribir si o no 
                                                                                    # y ese valor que se almacena en una variable se la convierte a minuscula para comparar
    if desea_continuar == "no":                                                     # Se compara el valor ingresado por el usuario con la string negativa "no"
        print("La ejecución del programa finalizó con éxito, muchas gracias")       # Se imprime un mensaje de finalización 
        exit()                                                                      # Se cierra la ejecución del programa
    elif desea_continuar == "si":                                                   # Capturo las el valor donde la variable sea igual al strin "si" para impedir que se ejecute con valores inválidos
        continuar_ejecucion
    else:                                                                           # Si el valor no es ni "si" ni "no" entonces se ejecuta esta sentencia el cual finaliza la ejecución del programa y,
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  # Muestra un mensaje de error
        exit()