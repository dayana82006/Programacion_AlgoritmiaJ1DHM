"""programa determina si unas longitudes pueden formar
un triángulo válido."""


def triangulos():
    ladoa = float(input('Ingrese la primera medida: '))
    ladob = float(input('Ingrese la segunda medida: '))
    ladoc = float(input('Ingrese la tercera medida: '))

    if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
        print('Se puede formar un triángulo válido.')
    else:
        print('No se puede formar un triángulo válido.')
if (__name__ == '__main__'):
    triangulos()