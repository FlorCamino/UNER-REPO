# Consigna

''' Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
derecho que al revés. Por ejemplo: rayar, kayak, somos ''' 

# Solución

texto_ingresado = input("Por favor, ingrese el texto: ").lower();
texto_invertido = texto_ingresado[::-1]

es_palindromo = texto_ingresado == texto_invertido
print("Es un texto palíndromo:" , es_palindromo)
