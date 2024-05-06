# Consigna
#  Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

def saludo(nombre):
    if nombre.isalpha():
        print(f"¡Hola {nombre}!") 
    else: 
        print("¡Error! El nombre no debe contener números ni caracteres especiales.") 
        saludo(input("Por favor indiquenos su nombre: ")) 
    
  
saludo(input("Por favor indiquenos su nombre: "))  
