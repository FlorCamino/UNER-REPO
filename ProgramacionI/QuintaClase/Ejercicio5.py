# Consigna
# Que dado tres números ingresados por el usuario nos devuelva el promedio.

def resultado_promedio(primer_valor, segundo_valor, tercer_valor): 
    return (primer_valor + segundo_valor + tercer_valor) / 3       


primer_numero =  float(input(f"Por favor ingrese el primer número: ")) 
segundo_numero =  float(input(f"Por favor ingrese el segundo número: "))
tercer_numero =  float(input(f"Por favor ingrese el tercer número: "))

print(f"El resultado del promedio de los 3 valores es: {resultado_promedio(primer_numero, segundo_numero, tercer_numero)}")  
                                                                                                                             
   
