# Consigna
# Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

def calcular_iva(cantidad, porcentaje=None):
    if porcentaje is None:
        porcentaje=21
    monto_iva = cantidad * (porcentaje / 100)
    return cantidad + monto_iva

monto_factura = float(input("Por favor ingrese el monto de la factura: \n"))
porcentaje_ingresado = input("Por favor ingrese el porcentaje a calcular: \n")
porcentaje= None
if porcentaje_ingresado.strip() != "": 
    porcentaje = int(porcentaje_ingresado)

resultado_iva = calcular_iva(monto_factura, porcentaje)
print("---------------------------------")
print("-------- Resultado Final --------")  
print(f"El valor resultante del {porcentaje if porcentaje is not None else 21}% del IVA al valor {monto_factura} es de {resultado_iva}" )