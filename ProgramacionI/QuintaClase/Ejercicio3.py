# Consigna
# Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

def calcular_iva(cantidad, porcentaje):
    monto_iva = cantidad * (porcentaje / 100)
    return cantidad + monto_iva

monto_factura = float(input("Por favor ingrese el monto de la factura "))
porcentaje = int(input("Por favor ingrese el porcentaje a calcular "))

print(f"El valor resultante del descuento de IVA es {calcular_iva(monto_factura, porcentaje)}" )