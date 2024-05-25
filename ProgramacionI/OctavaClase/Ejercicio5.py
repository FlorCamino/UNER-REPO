
# Consigna
# Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
# usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
# de los números ingresados por el usuario deberá ser almacenado en una lista. A
# continuación, realice las siguientes tareas:
#       a. Determinar el máximo.
#       b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#       c. Determinar el mínimo.
#       d. Calcular la multiplicación de todos los números de la lista.
#       e. Contar los valores pares e impares.
#       f. Remover los elementos repetidos.

numeros_almacenados = []

while True:
    entrada = input("Por favor, ingrese un número entero o escriba 'fin' para terminar: ")
    if entrada.lower() == 'fin':
        break
    try:
        numero_ingresado = int(entrada)
        numeros_almacenados.append(numero_ingresado)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

def multiplicar_elementos(lista_numeros):
    resultado_multiplicacion = 1
    for elemento in lista_numeros:
        resultado_multiplicacion *= elemento
    print(f"El resultado de la multiplicación de los elementos es {resultado_multiplicacion}")
    print()

def contar_par_impar(lista_numeros):
    contador_par = sum(1 for numero in lista_numeros if numero % 2 == 0)
    contador_impar = len(lista_numeros) - contador_par
    print(f"Hay un total de {contador_par} números pares y {contador_impar} números impares")
    print()

def remover_repetidos(lista_numeros):
    lista_sin_repetidos = list(set(lista_numeros))
    print(f"La lista sin elementos repetidos es {lista_sin_repetidos}")
    print()

print("---------------------------------")
print("-------- Resultado Final --------\n")
if numeros_almacenados:
    print("-------- Valor máximo --------")
    print(f"El valor máximo de la lista es {max(numeros_almacenados)}\n")

    print("-------- Segundo valor máximo --------")
    numeros_ordenados = sorted(numeros_almacenados)
    if len(numeros_ordenados) >= 2:
        print(f"El segundo valor máximo de la lista es {numeros_ordenados[-2]}\n")
    else:
        print("No hay suficientes elementos en la lista para calcular el segundo valor máximo.\n")

    print("-------- Valor mínimo --------")
    print(f"El valor mínimo de la lista es {min(numeros_almacenados)}\n")

    print("-------- Multiplicación de elementos --------")
    multiplicar_elementos(numeros_almacenados)

    print("-------- Contar números par e impar --------")
    contar_par_impar(numeros_almacenados)

    print("-------- Eliminar los elementos repetidos --------")
    remover_repetidos(numeros_almacenados)
else:
    print("No se han ingresado números.")