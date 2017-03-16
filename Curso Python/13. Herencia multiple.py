#Se crea la clase
class Humano:
    def __init__(self, edad):
        self.edad = edad
    def saludo(self, mensaje):
        print mensaje
        print '////////////////////'

class IngenieroSistemas(Humano):
    def __init__(self,escuela):
        print 'estudie en la escuela: ', escuela
    def programar(self,lenguaje):
        print 'se programar en: ',lenguaje

class LicenciadoDerecho(Humano):
    def __init__(self):
        print 'madres'
    def estudiarCaso(self,caso):
        print 'Voy a leer el caso: ',caso

#ASI ES QUE SE DA LA HERENCIA MULTIPLE
    #recuerda que si las dos clases de donde heredan tienen metodo __init__ siempre va a coger el metodo __init__
    #de la primer clases que en este caso es IngenieroSistemas y no utilizara el de LicenciadoDerecho
class estudioso(IngenieroSistemas, LicenciadoDerecho):
    #la palabra pass es como de pase siga
    pass


pepe = estudioso('Universidad Libre Cali')
pepe.programar('python')
pepe.estudiarCaso('del abogado')
pepe.saludo('Hola muchachos locos')