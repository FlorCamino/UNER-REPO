
# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def calcular_potencia(base, exponente): # Función que recibe como parámetros base y exponente,
    return base ** exponente             # y retorna el resultado de la potencia

valor_ingresado_base = int(input("Ingresar el valor base de la potencia: ")) # Solicitud de los valores por consola 
valor_ingresado_exponente =  int(input("Ingresar el valor exponente de la potencia: ")) # y casteados a tipo integer
                                                                               
print(f"El resultado final de la potencia es {calcular_potencia(valor_ingresado_base, valor_ingresado_exponente)}") # Impresión del valor final por consola invocando la función y 
                                                                                                                # pasando las varibles ingresadas como argumento, luego se asigna
                                                                                                                #  a una variable su valor
