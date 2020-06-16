def positivoNegativo(numero):
    if numero > 0 :
        print('     positivo')
    elif numero == 0:
        print('     es cero')
    else:
        print('     negativo')


def parImpar(numero):
    if numero==0:
        print('     es cero')
    elif numero%2:
        print('     impar')
    else:
        print('     par')


def primo(numero):
    if numero>0:
        if numero==2 or numero==3 or numero==5 or numero ==7:
            print('     primo')
        elif numero%2==0 or numero%3==0 or numero%5==0 or numero%7==0:
            print('     no primo')
        else:
            print('     primo')
    elif numero==0 :
        print('     igual a cero')
    else:
        print('     menor a cero')

def anioBiciesto(anio):
    if anio>0:
        if anio%4==0:
            if anio%100!=0 or anio%400==0:
                print('anio bisiesto')
        else:
            print('anio no bisiesto')
    else:
        print('anio no valido')



if __name__=='__main__':
    numero =int(input('ingresa un numero entero '))
    print('numero ')
    positivoNegativo(numero)
    parImpar(numero)
    primo(numero)


