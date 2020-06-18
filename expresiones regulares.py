import re

def validaCorreo(correo):
    for i in correo:
        if re.search("@python.padts.mx$|@padts.com.mx$|@padts.mx$",i)is not None:
            print(i," correo valido")
        else:
            print(i," correo No valido")


def numtel(numero):
    for j in numero:
        if re.search('[0-9]{10}|\([0-9]{2,3}\)[0-9]{7,8}|\([0-9]{2,3}\)[ -]?[0-9]{3,4}[ -]?[0-9]{4}$',j)is not None:
            print(j,' numero valido')
        else:
            print(j,' numero No valido')


def rfcin(rfc):
    for k in rfc:
        if re.search('[A-Z]{4}[0-9]{6}[A-Z0-9]{5}[A-Z0-9]{2}$',k)is not None:
            print(k,' RFC valido')
        else:
            print(k,' RFC No valido')


def CURP(curp):
    for l in curp:
        if re.search('[A-Z]{4}[0-9]{6}[HM][A-Z]{3}',l)is not None:
            print(l,' CURP valido')
        else:
            print(l,' CURP No valido')


print('\n validacion de correos \n')
correo = 'juan@padts.mx','juan@padts.com.mx','juan@python.padts.mx'
validaCorreo(correo)

print('\nvalidacion de numeros\n')
numero= '331234678','(33)12345678','(331)12345678','(33)1234 5678','(331)123-5678'
numtel(numero)

print('\nvalidacion de RFC\n')
rfc= 'FRTY987654JGTDK98','GTYU98567HJUPLO4'
rfcin(rfc)

print('\nvalidacion de CURP\n')
curp='HJUI987654HMKJ04','OKL7897M'
CURP(curp)