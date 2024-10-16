"""Este programa luego muestre la tabla
de multiplicar un número del 1 al 10"""


def tablaM(num):
    print(f'\nTabla de multiplicar del {num}:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')


numeroU = int(input('Ingresa un número: '))

if (__name__ == '__main__'):
    tablaM(numeroU)