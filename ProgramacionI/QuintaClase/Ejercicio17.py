# Consigna
# Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay
        
def es_primo(valor_constante):
    es_primo = True
    if valor_constante <= 1:
        es_primo = False
    for numero in range(2, int(valor_constante**0.5) + 1):
        if valor_constante % numero == 0:
            es_primo = False
    return es_primo

def imprimir_primos_y_contar():
    contador = 0
    primer_primo = True
    for numero in range(101):
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