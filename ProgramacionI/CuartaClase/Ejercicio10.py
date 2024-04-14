# Consigna

''' Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
derecho que al revés. Por ejemplo: rayar, kayak, somos ''' 

# Solución

textoIngresado = input("Por favor, ingrese el texto: ").lower()
textoInvertido = textoIngresado.lower()[::-1]

if textoInvertido == textoIngresado:
    print("Es un texto palíndromo")
else: 
    print("No es un texto palíndromo")