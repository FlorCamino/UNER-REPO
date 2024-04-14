# Consigna

'''  Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985 ''' 

# Solución

nombreUsuario = input("Por favor, indique su nombre: ")
apellidoUsuario = input("Indique su apellido: ")
anioNacimiento = input("Ahora, ingrese su año de nacimiento: ")

inputSugerencia = f"Nombre: {nombreUsuario}\n"
inputSugerencia += f"Apellido: {apellidoUsuario}\n"
inputSugerencia += f"Año nacimiento: {anioNacimiento}\n"
inputSugerencia += f"Usuario: {nombreUsuario[0]}{apellidoUsuario}\n"
inputSugerencia += f"Contraseña: {nombreUsuario[0]}{apellidoUsuario[0]}.{anioNacimiento}"

print(inputSugerencia)

                