
#este programa determina si un usuarrio a aprobado o reprobadoç

def calificacion():
 nota=float(input('Ingrese la nota: '))
 if nota >= 60:
    print('Has aprobado')
 else:
    print('Has reprobado')
    
if (__name__ == '__main__'):
 calificacion()