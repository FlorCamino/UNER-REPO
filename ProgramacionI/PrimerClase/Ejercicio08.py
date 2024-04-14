# Consigna

''' Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
luego imprimir por pantalla la superficie total ''' 

# Solución

baseTriangulo = float(input("Por favor, ingrese la base del triángulo: "))
alturaTriangulo = float(input("Ahora, ingrese la altura del triángulo: "))

superficieTriangulo = (baseTriangulo * alturaTriangulo) / 2

print(f"La superficie del triángulo es {superficieTriangulo} cm2")