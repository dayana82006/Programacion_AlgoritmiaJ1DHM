
def total():
    consumo = input("Ingrese el mes de consumo: ")
    valorKw = float(input("Ingrese el valor del KW: "))
    totalKw = float(input("Ingrese el total de KW consumidos en el mes: "))
    estrato = input("Ingrese el estrato: ")

    valorTotal = valorKw * totalKw

    print(f"Mes de consumo: {consumo}")
    print(f"Valor por KW: {valorKw}")
    print(f"Total KW consumido: {totalKw}")
    print(f"Estrato: {estrato}")
    print(f"Valor a pagar por energía eléctrica: {valorTotal}")

if (__name__ == '__main__'):
    total()