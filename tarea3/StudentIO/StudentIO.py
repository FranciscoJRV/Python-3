try:
    import cPickle as pickle
except ImportError:
    import pickle
import shelve

class estudiante(): #ifoperssonas = estusiantes
    __nombre = ''
    __correo = '' #fechanacimiento=corero
    __contrasena = '' #lugarnacimiento= contrasena

    def __init__(self, nom, corr, cont): #n=nom fn=corr ln=cont
        self.__nombre = nom
        self.__correo = corr
        self.__contrasena = cont

    def Nombre(self):
        return self.__nombre

    def Correo(self):
        return self.__correo

    def Contrasena(self):
        return self.__contrasena

    def __str__(self):
        return f'Nombre: {self.__nombre}\n' \
               f'Correo: {self.__correo}\n' \
               f'Contrasena: {self.__contrasena}'

nombres = ['Frank', 'Javier', 'Diana', 'Laura','Naomi']
correos = ['f@live.com', 'j@live.com', 'd@live.com', 'l@live.com', 'n@live.com']
contrasenas = ['f12', 'j23', 'd34', 'l45', 'n56']

alumno = []
def asignacion():

    for n, c, ct in zip(nombres, correos, contrasenas):
        alumno.append(estudiante(n, c, ct))


def readStudentp():
    for i in alumno:
            print(i)


#asignacion()
#readStudentp()

#Abrir archivo modo escritura, peackle

def saveStudentP():
    file = open('alumnos.db', 'wb')
    pickle.Pickler(file, 4).dump(alumno)
    file.close()


#saveStudentP()

def abrirArchivop():
    file = open('alumnos.db', 'rb')
    unpickler = pickle.Unpickler(file)
    alumnos = unpickler.load()
    file.close()

#abrirArchivop()


def saveStudents():
    with shelve.open('Estudiantes.db','wb',) as file:
        for n, c, ct in zip(nombres,correos,contrasenas):
            alumno.append(estudiante(n,c,ct))


def readStudents():
    with shelve.open('Estudiantes.db', 'rb') as file:
        file=alumno
        for j in file:
            print(j)

#saveStudents()
#readStudents()