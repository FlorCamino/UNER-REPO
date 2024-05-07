# Consigna
# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def calcular_potencia(base, exponente): 
    return base ** exponente             

valor_ingresado_base = int(input("Ingresar el valor base de la potencia: ")) 
valor_ingresado_exponente =  int(input("Ingresar el valor exponente de la potencia: "))

resultado_potencia = calcular_potencia(valor_ingresado_base, valor_ingresado_exponente)
print("---------------------------------")
print("-------- Resultado Final --------")                                                                       
print(f"El resultado final de la potencia es {resultado_potencia}") 
