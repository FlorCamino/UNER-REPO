import sys
"""EJERCICIO 1
        Escribe un programa que lea las calificaciones de un grupo de estudiantes (el usuario ingresará las
        calificaciones una a una y usará el valor “FIN” para finalizar la entrada de datos). El programa debe
        cumplir con los siguientes requisitos:
        
        Requisitos:
            ● Utilizar una lista para almacenar las calificaciones.
            ● Imprimir las calificaciones ordenadas de menor a mayor.
            ● Calcular y mostrar el promedio por pantalla.
            ● Contar el número de calificaciones ingresadas.
            ● Convertir todas las calificaciones a strings y unirlas en una sola cadena(string) separada
            por comas.
            ● Contar cuántos alumnos han aprobado la materia (sacaron una nota mayor o igual a 6).
            ● Calcular la calificación más baja y la más alta e Imprimir por pantalla un mensaje con el
            siguiente formato: “La calificación más baja fue XX y la más alta XX.”
            ● Vaciar la lista."""
            
lista_calificaciones = []
terminar = ''


def ingresar_calificaciones():
    continuar = True
    while continuar:
        calificacion = float(input("Por favor, ingrese las calificaciones de los estudiantes:\n"))
        lista_calificaciones.append(calificacion)
        desea_continuar = input("¿Desea continuar? SI/NO \n").lower()
        if desea_continuar == 'no':
            continuar = False
        elif desea_continuar == 'si':
            continuar = True
        else:
            print("¡El valor ingresado no es correcto! El programa finalizará")
            sys.exit()
    print()
    
def imprimir_lista_calificaciones(lista):
    i = 1
    for calificacion in sorted(lista):
        print(f"{i}. {calificacion}") 
        i+=1
    print()
        
    
def calcular_promedio(lista):
    contador = sumar_calificaciones = 0
    for calificacion in lista:
        sumar_calificaciones += calificacion
        contador+=1
        promedio = sumar_calificaciones / contador
    print(f"El promedio es {promedio}")
    print()
        
def convertir_a_string(lista):
    contador = 0
    es_ultimo = len(lista) - 1
    for calificacion in lista:
        if es_ultimo != contador:
            print(str(calificacion) + ", ", end='')
        else:
            print(str(calificacion))
        contador+=1
    print()
            
def alumnos_aprobados(lista):
    contador = 0
    for calificacion in lista:
        if calificacion >= 6:
                contador+=1        
    print(f"Un total de {contador} alumnos han aprobado la materia")
    print()
    
def mejor_menor_nota(lista):
    print(f"La calificación más baja fue {min(lista)} y la más alta {max(lista)}.")
    print()
        
while terminar != 'fin':     
    print("------------ Ingresar calificaciones -------------\n")
    ingresar_calificaciones()
    print("--------- Imprimir calificaciones ordenadas ---------\n")
    imprimir_lista_calificaciones(lista_calificaciones)
    print("-------------- Calcular promedio ---------------\n")
    calcular_promedio(lista_calificaciones)
    print("--------- Contar calificaciones ingresadas ----------\n")
    print(f"La cantidad de calificaciones ingresadas es {len(lista_calificaciones)}\n")
    print("------------ Convertir a string -------------\n")
    convertir_a_string(lista_calificaciones)
    print("------------ Cantidad alumnos aprobados -------------\n")
    alumnos_aprobados(lista_calificaciones)
    print("------------ Mejor y menor calificación -------------\n")
    mejor_menor_nota(lista_calificaciones)
    print("---------- Limpiar lista de calificaciones -----------\n")
    lista_calificaciones.clear()
    
    valor = input("¿Desea terminar con la ejecución? Escriba 'fin'\n").lower()
    if valor == 'fin':
        print("El programa finalizó. ¡Muchas gracias!")
        terminar = valor
        