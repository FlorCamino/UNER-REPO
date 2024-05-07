# Consigna
# Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay
        
def es_primo(valor_constante):
    es_primo = True
    if valor_constante <= 1:
        es_primo = False
    for numero in range(2, int(valor_constante**0.5) + 1): # Disminuimos la cantidad de comprobaciones supongamos que ingresamos 37, la raiz del mismo es 6.08, 
        if valor_constante % numero == 0:                  # entonces debemos comprobar que si 37 % (2,3,4,5,6) no es divisible por ellos entonces es primo
            es_primo = False
    return es_primo

def imprimir_primos_y_contar():
    contador = 0
    primer_primo = True
    VALOR_MAXIMO = 100
    print("---------------------------------")
    print("-------- Resultado Final --------")    
    for numero in range(VALOR_MAXIMO):
        if es_primo(numero):
            if primer_primo:
                print(numero, end="")
                primer_primo = False
            else:
                print(", ", numero, end="")
            contador += 1
    print() 
    print(f"El total de números primos es de {contador}")
    exit()   

imprimir_primos_y_contar()