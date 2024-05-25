
# Consigna
# Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
# muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario)

continuar_ejecucion = True  
materias = ["Programación I","Introducción a la informática", "Diseño Gráfico","Arquitectura de las Computadoras", "Programación II", "Sistemas Operativos", "Introducción al Desarrollo Web", "Bases de Datos", "Redes de Datos", "Programación III", "Ingenieria de Software", "Desarrollo de Aplicaciones Web", "Desarrollo para Móviles", "Multimedia y Juegos en Web"]

def imprimir_materias(materias):
    contador= 1; 
    for materia in materias:
        print(contador, "-", materia)
        print()
        contador += 1

print("---------------------------------")
print("-------- Resultado Final --------") 
while continuar_ejecucion:
    imprimir_materias(materias)
    respuesta_usuario = input("¿Desea continuar listando las materias? SI/NO \n").lower()
    if respuesta_usuario == "no":
        exit()
    elif respuesta_usuario == "si":                                           
        continuar_ejecucion
    else:                                                                   
        print("Fin de la ejecución, ha ocurrido un error debido a que el valor ingresado no está permitido")  
        exit()
