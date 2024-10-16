

#este programa verifica si se cumplen con ciertos requisitos 

def contraseña():
    contraseñaU=str(input('Ingrese una contraseña que contenga minimo 8 digitos y 1 numero: '))
    total=len(contraseñaU)
    numeros= "0123456789"
    totalN=False

    for i in contraseñaU:
            for i in numeros:
                 totalN=True
                    
                    
    if total >=8 and totalN==True : 
     print('Su contraseña ha sido guardada correctamente')
    else:
     print('Su contraseña es invalida')
if (__name__ == '__main__'):
 contraseña()
