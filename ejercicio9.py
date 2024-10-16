"""programa calcula e imprime el promedio de los
números ingresados"""
def Promedio():
    suma = 0
    total = 0

    while True:
        numero = float(input("Ingresa un número para promediar que sea positivo: "))
        
        if numero < 0:
            break
        
        suma += numero
        total += 1

    if total > 0:
        print("Promedio:", suma / total)
    else:
        print("Ingrese nuemoros correctos.")

if (__name__ == '__main__'):
    Promedio()