        #Herencia y polimorfismo:
#Definir una clase Figura con atributos y métodos.
#Definir una clase rectángulo que hereda de figura.
#Definir una clase Triángulo que hereda de figura.
class figura():
    def __init__(self, base, altura):
        self.base = base
        self.altura=altura

    def area(self):
        are= self.base * self.altura
        return are

    def perimetro(self):
        per= (self.base + self.altura)*2
        return per


class cuadrado(figura):
    def __init__(self,base,altura):
       super().__init__(base,altura)


class triangulo(figura):
    def __init__(self,base,altura):
       super().__init__(base,altura)
    def area(self):
        areat=(self.base*self.altura)/2
        return areat

cuadra=cuadrado(12,2)
print('El area del cuadrado es',cuadra.area())
print('El perimetro del cuadrado es ',cuadra.perimetro())
tring=triangulo(3,4)
print('El area del triangulo es ',tring.area())
print('El perimetro del triangulo es ',tring.perimetro())

        #Encapsulación
#Crear una clase estudiante son atributos: nombre, correo electrónico y contraseña.
#Crear métodos para ingresar y obtener los atributos.
import poplib

class estudiante():
    __nombre=''
    __correo=''
    __contrasena=''

    def ingresarDatos(self):
        self.__nombre=input('Ingrsa nombre: ')
        self.__correo = input('ingrsa correo: ')
        self.__contrasena = input('ingrsa contraseña: ')
        return self.__nombre
        return self.__correo
        return self.__contrasena

    def obtenerDatos(self):
        print('\nImpresion de los datos adquiridos\n')
        print('nombre ',self.__nombre)
        print('correo ', self.__correo)
        print('contraseña ', self.__contrasena)

Alumno1=estudiante()
Alumno1.ingresarDatos()
Alumno1.obtenerDatos()