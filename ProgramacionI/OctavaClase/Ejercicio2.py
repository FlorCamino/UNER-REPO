
# Consigna
# Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado

continuar_ejecucion = True  
numeros_ingresados = []

def ingresar_numeros(lista_numeros):
    numero = 0
    while numero <= 4:
        numero_ingresado = int(input("Por favor, ingrese un números: \n"))
        lista_numeros.append(numero_ingresado)
        numero += 1

def ordernar_y_mostrar_numeros(numeros_ingresados):
    print("---------------------------------")
    print("-------- Resultado Final --------")
    print(f"Los números ingresados son: {numeros_ingresados}")
    numeros_ingresados.sort()
    print(f"Los números ordenados: {numeros_ingresados}")
           
while continuar_ejecucion:
    ingresar_numeros(numeros_ingresados)
    ordernar_y_mostrar_numeros(numeros_ingresados)
    respuesta_usuario = input("¿Desea continuar ingresando números? SI/NO \n").lower()
    if respuesta_usuario == "no":
        exit()
    elif respuesta_usuario == "si":                                           
        continuar_ejecucion
    else:                                                                   
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()
