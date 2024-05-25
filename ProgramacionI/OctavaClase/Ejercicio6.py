
# Consigna
# Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
# de una lista vacía:
#       a. Agregar un elemento al final.
#       b. Agregar un elemento al principio.
#       c. Quitar un elemento al final.
#       d. Quitar un elemento al principio.

lista_elementos = []
lista = []
primer_ejecucion = True
ejecucion_activa = True

def agregar_elemento_final(lista_elementos):
    ultimo_elemento = input("Por favor, ingrese el elemento: ")
    lista_elementos.append(ultimo_elemento)
    return lista_elementos
    
def agregar_elemento_principio(lista_elementos):
    primer_elemento = input("Por favor, ingrese el elemento: ")
    lista_elementos.insert(0,primer_elemento)
    return lista_elementos
    
def quitar_elemento_final(lista_elementos):
    lista_elementos.pop()
    return lista_elementos
    
def quitar_elemento_principio(lista_elementos):
    del lista_elementos[0]
    return lista_elementos 

while ejecucion_activa:
    print("¿Qué desea hacer? Ingrese la letra correspondiente: ")
    print("a. Agregar un elemento al final.")
    print("b. Agregar un elemento al principio.")
    if not primer_ejecucion:
        print("c. Quitar un elemento al final.")
        print("d. Quitar un elemento al principio.")
        print("e. Mostrar la lista y salir.")
    letra = input()

    if len(letra) == 1:
        match(letra):
            case "a":
                lista = agregar_elemento_final(lista_elementos) 
            case "b":
                lista = agregar_elemento_principio(lista_elementos)
            case "c":
                lista = quitar_elemento_final(lista_elementos) 
            case "d":
                lista = quitar_elemento_principio(lista_elementos)
            case "e":
                print(f"La lista con la modificación ingresada es {lista}")
                exit()  
            case _: 
                print("La letra no coincide con el menú")
                
    primer_ejecucion = False






