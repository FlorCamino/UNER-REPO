
# Consigna
# Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
# con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
# usuario:
#       a. Agregar nuevas tareas pendientes.
#       b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
#           de la lista de pendientes a la de terminadas.
# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
# listas.

tareas_pendientes_lista = []
tareas_terminadas_lista =  []
continuar_ejecucion = True

def agregar_tareas_pendientes(tareas_pendientes_lista):
    tarea_ingresada = ""
    tarea_ingresada = input("Por favor, ingrese la tarea pendiente: ").strip().lower()
    if tarea_ingresada != "":
       tareas_pendientes_lista.append(tarea_ingresada)
    mostrar_estado_listas(tareas_pendientes_lista, tareas_terminadas_lista)

def marcar_tareas_terminadas(tareas_pendientes_lista, tareas_terminadas_lista):
    print("------------- Resultado --------------")
    tarea_terminada = input("Por favor, ingrese las tareas que ha finalizado: ").strip().lower()
    if tarea_terminada in tareas_terminadas_lista:
        print(f"La tarea '{tarea_terminada}' ya está marcada como terminada.") 
    elif tarea_terminada in tareas_pendientes_lista:
        tareas_terminadas_lista.append(tarea_terminada)
        tareas_pendientes_lista.remove(tarea_terminada)
    else:
        print(f"La tarea '{tarea_terminada}' no existe en la lista de tareas pendientes.")
    mostrar_estado_listas(tareas_pendientes_lista, tareas_terminadas_lista) 
        
def mostrar_estado_listas(tareas_pendientes_lista, tareas_terminadas_lista):
    print("------------- Listas --------------")
    print(f"Tareas pendientes: {tareas_pendientes_lista}")
    print(f"Tareas terminadas: {tareas_terminadas_lista}")
    print()

while continuar_ejecucion:
    print("¿Qué desea hacer?")
    print("a. Agregar nuevas tareas pendientes.")
    print("b. Marcar tareas pendientes como terminadas.")
    print("c. Salir del programa.")
    opcion = input("Ingrese la opción correspondiente: ").lower()

    if opcion == "a":
        agregar_tareas_pendientes(tareas_pendientes_lista)
    elif opcion == "b":
        marcar_tareas_terminadas(tareas_pendientes_lista, tareas_terminadas_lista)
    elif opcion == "c":
        tareas_terminadas_lista.clear()
        tareas_pendientes_lista.clear()
        exit()
    else:
        print("Opción inválida. Por favor, ingrese 'a', 'b' o 'c'.")

print("El programa a finalizado con exito ¡Muchas gracias!")