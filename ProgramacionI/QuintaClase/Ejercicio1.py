# Consigna
#  Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

def saludo(nombre):
    if nombre.isalpha():
        print(f"¡Hola {nombre}!") #Imprimo el valor de nombre cuando el mismo es un valor de tipo alfabético
    else: 
        print("¡Error! El nombre no debe contener números ni caracteres especiales.") # Muestro mensaje de error
        saludo(input("Por favor indiquenos su nombre: ")) # Se instancia nuevamente la función para que se ejecute 
                                                          # hasta que indique un valor correcto
    
  
saludo(input("Por favor indiquenos su nombre: "))  # Instancia de la función para que se ejecute
