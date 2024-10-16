"""Este programa
permite ingresar la información de un
empleado """
def datos():
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese los apellidos: ')
    edad = int(input('Ingrese edad: '))
    telefono = int(input('Ingrese telefono: '))
    antiguedad = int(input('Digite hace cuanto ingreso: '))

   
    print(f"El nombre es: {nombre} {apellidos}, tiene {edad} años, su teléfono es {telefono}, y tiene {antiguedad} años de antigüedad.")
if (__name__ == '__main__'):
    datos()