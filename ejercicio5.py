    #este programa te dice a que continente pertenece un pais
def continentes():
        pais=input('Ingrese un país: ')
        if pais in ('argentina', 'brasil', 'colombia', 'panama', 'chile'):
                print ('El país es de Sur America')
        
        elif pais in('dinamarca', 'francia', 'alemania', 'italia'):
            print ('El país es de Europa')
        elif pais in ('china', 'japón', 'india'):
                print ('El país es de Asia')
        elif pais in ('méxico','canadá', 'estados unidos'):
                print ('El país es de NorteAmerica')
        elif pais in ('australia', 'nueva zelanda'):
                print ('El país es de Oceanía')
        elif pais in ('egipto', 'sudáfrica', 'Burundi'):
                print ('El país es de África')
        else:
                print ('El país no se encuentra')

if (__name__ == '__main__'):
        continentes()