# Consigna

'''  Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985 ''' 

# Solución

nombre_usuario = input("Por favor, indique su nombre: ")
apellido_usuario = input("Indique su apellido: ")
anio_nacimiento = input("Ahora, ingrese su año de nacimiento: ")


print("Usuario: " + nombre_usuario[0] + apellido_usuario)
print("Contraseña: " + nombre_usuario[0] + apellido_usuario[0] + "." + str(anio_nacimiento))

                