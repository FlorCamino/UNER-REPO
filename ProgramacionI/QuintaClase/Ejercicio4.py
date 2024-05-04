# Consigna
# Que dada la base y altura de un triángulo nos calcule su área.

def calcular_area(base, altura):        # Función que calcula el área y recibe como parámetros
    return int((base * altura) / 2)     # base y altura y retorna el resultado del área de un triángulo

base = int(input("Por favor, ingrese la base de su triángulo "))
altura = int(input("Por favor, ingrese la altura de su triángulo "))   # Solicitud de los valores al usuario por consola

print(f"El área de un triángulo de base {base} y altura {altura} es de {calcular_area(base, altura)} ") # Imprime el valor final instanciando a la función
                                                                                                        # y enviando como argumento los valores ingresados por el usuario