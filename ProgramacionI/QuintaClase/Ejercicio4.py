# Consigna
# Que dada la base y altura de un triángulo nos calcule su área.

def calcular_area(base, altura):        
    return int((base * altura) / 2)     

base = int(input("Por favor, ingrese la base de su triángulo "))
altura = int(input("Por favor, ingrese la altura de su triángulo "))  

print(f"El área de un triángulo de base {base} y altura {altura} es de {calcular_area(base, altura)} ") 