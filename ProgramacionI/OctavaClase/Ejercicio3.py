
# Consigna
# Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
# frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
# debajo la misma lista pero sólo con las frutas que añadió el usuario.

continuar_ejecucion = True  
frutas = ["banana", "manzana", "pera"]

def agregar_fruta(lista_fruta):
    numero = 0
    while numero <= 2:
        fruta_ingresada = input("Por favor, ingrese una fruta: \n")
        lista_fruta.append(fruta_ingresada)
        numero += 1
           


while continuar_ejecucion:
    agregar_fruta(frutas)
    
    print("---------------------------------")
    print("-------- Resultado Final --------") 
    print(f"La lista completa de fruta es {frutas}")
    print(f"Las fruta ingresadas fueron {frutas[-3:]}")
    respuesta_usuario = input("¿Desea continuar ingresando números? SI/NO \n").lower()
    if respuesta_usuario == "no":
        exit()
    elif respuesta_usuario == "si": 
        del frutas[-3:]                                          
        continuar_ejecucion
    else:                                                                   
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()
