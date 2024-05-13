# Consigna
# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def calcular_potencia(base, exponente): 
    return base ** exponente             

valor_ingresado_base = int(input("Ingresar el valor base de la potencia mayor a 0: ")) 
valor_ingresado_exponente =  int(input("Ingresar el valor exponente de la potencia mayor a cero: "))
if valor_ingresado_base > 0:
    if valor_ingresado_exponente > 0: 
        resultado_potencia = calcular_potencia(valor_ingresado_base, valor_ingresado_exponente)
        print("---------------------------------")
        print("-------- Resultado Final --------")                                                                       
        print(f"El resultado final de la potencia es {resultado_potencia}") 
    else:
        print(f"¡Error! El número {valor_ingresado_exponente} no es positivo")  
else:
    print(f"¡Error! El número {valor_ingresado_base} no es positivo")

