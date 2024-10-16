#este programa nos dice si una fecha es valida o no


def  fecha_valida():
    diaU=int(input('Ingrese el dia: '))
    mesU=int(input('Ingrese el mes en numero: '))
    añoU=int(input('ingrese el año: '))
    if mesU == 4 or mesU == 6 or mesU == 9 or mesU == 11:
        if diaU <= 30:
            if añoU<= 2024:
                print('La fecha es valida')
            else:
                print('La fecha no es valida ')
        else:
            print('La fecha no es valida')
    if mesU == 1 or mesU == 3 or mesU == 5 or mesU == 7 or mesU == 8 or mesU == 10 or mesU == 12:
        if diaU <=31:
            if añoU<=2024:
                print('La fecha es valida')
            else:
                print('La fecha no es valida ')
        else:
            print('La fecha no es valida')
    if mesU==2:
        if diaU<=29:
            if añoU % 4 == 0 or añoU % 400 == 0:
                print('La fecha es valida')
            else:
                print('La fecha no es valida ')
        else:
            print('La fecha no es valida')
            
if (__name__ == '__main__'):
    fecha_valida() 
            