

#este programa determina si el usuario es menor o mayor de edad 
def edades():
  edad=int(input('Ingrese una edad: '))
  if edad<18:
    print('usted es menor de edad')
  else:
    print('Usted es mayor de edad') 

edades()