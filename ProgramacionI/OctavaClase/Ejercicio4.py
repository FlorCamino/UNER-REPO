
# Consigna
# Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
# realizar lo siguiente:
#       a. Imprimir la cantidad de elementos que tiene la lista.
#       b. Imprimir el primer y último elemento.
#       c. Imprimir el resto.
#       d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#           la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#       e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#           la lista. Quitar el elemento correspondiente de esa posición.
#       f. Imprimir la lista en orden inverso.
#       g. Vaciar la lista.

continuar_ejecucion = True  
paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

def ingresar_pais(lista_paises):
    lista_paises_minusculas = list(map(str.lower, lista_paises))
    pais_ingresado = input("Por favor, ingrese un país: \n").strip().lower()
    if pais_ingresado in lista_paises_minusculas:
        posicion = lista_paises_minusculas.index(pais_ingresado)
        print(f"El pais {pais_ingresado} se encuentra en la posición {posicion}")
    else:
        print(f"El pais {pais_ingresado} NO se encuentra en la lista")
    print()
           
def eliminar_pais(lista_pais):
    continuar_ingresando = True
    while continuar_ingresando:
        indice_ingresado = int(input("Por favor, ingrese un número del 0 al 4: \n"))
        if 0 <= indice_ingresado < len(lista_pais):
            continuar_ingresando = False
        
    if indice_ingresado <= len(lista_pais):
        del lista_pais[indice_ingresado]
        print(f"Se elimino el indice, el resultado final es {lista_pais}")
    else:
        print(f"El indíce ingresado {indice_ingresado} no coincide con los elementos de la lista")
    print()
       
while continuar_ejecucion:
    print("---------------------------------")
    print("-------- Resultado Final --------\n") 
    print("-------- Longitud de lista --------") 
    print(f"La cantidad de paises en la lista es de {len(paises)}\n")
    print("-------- Primer y último elemento de la lista --------") 
    print(f"El primer elemento en la lista es {paises[0]} y el último es {paises[-1]}\n")
    print("-------- Resto elementos --------") 
    print(f"El resto de países es: {paises[1:-1]}\n")
    print("-------- Retornar posición de un elemento --------") 
    ingresar_pais(paises)
    print("-------- Eliminar un pais de la lista --------") 
    eliminar_pais(paises)
    print("-------- Invertir la posición de los elementos en la lista --------") 
    paises.reverse()
    print(f"Los paises invertidos son {paises}\n")
    print("-------- Lista vacía --------") 
    paises.clear()
    print(f"La lista de paises se ha limpiado \n")
    
    respuesta_usuario = input("¿Desea continuar ingresando números? SI/NO \n").lower()
    if respuesta_usuario == "no":
        exit()
    elif respuesta_usuario == "si":                                          
        continuar_ejecucion
    else:                                                                   
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()

