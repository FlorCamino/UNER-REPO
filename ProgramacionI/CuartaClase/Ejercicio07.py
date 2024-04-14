# Consigna

''' Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
segundos son esos números de días ''' 

# Solución

numeroDias = int(input("Por favor, ingrese el número de dias que desea calcular: "))

calcularHoras = (numeroDias * 12)
calcularMinutos = calcularHoras * 60
calcularSegundos = calcularMinutos * 60

print(f"El número de {numeroDias} días, representa un total de {calcularHoras}hs, {calcularMinutos}min y {calcularSegundos}seg.")

