
# Que dado tres números ingresados por el usuario nos devuelva el promedio.

def resultado_promedio(primer_valor, segundo_valor, tercer_valor): # Función que recibe 3 valores numericos como parámetros
    return (primer_valor + segundo_valor + tercer_valor) / 3       # retorna el resultado del promedio de todos los números


primer_numero =  float(input(f"Por favor ingrese el primer número: ")) # Ingreso de variables por consola
segundo_numero =  float(input(f"Por favor ingrese el segundo número: "))
tercer_numero =  float(input(f"Por favor ingrese el tercer número: "))

print(f"El resultado del promedio de los 3 valores es: {resultado_promedio(primer_numero, segundo_numero, tercer_numero)}")  # Muestra por consola el resultado final
                                                                                                                            # instanciando la función y pasando como 
                                                                                                                            # argumento las variables que ingreso el 
                                                                                                                            # usuario 
   
