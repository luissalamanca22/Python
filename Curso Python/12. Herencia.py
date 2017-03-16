#Se crea la clase
class Humano:
    #se crea un metodo por defecto que es el primero que se inicializa, al igual que el parameto self
    def __init__(self, edad):
        #aqui creamos los atributos de la clase
        self.edad = edad

    def saludo(self, mensaje):
        print mensaje
        print '////////////////////'

#para heredar se escribe class NombreClase(ClaseHereda)
class IngenieroSistemas(Humano):
    #si en esta clase no hay ningun metodo __init__ lo hereda de la clase padre
    #si en esta clase se especifica el metodo __init__ no hereda el metodo __init__ de clase madre
    def __init__(self):
        print 'soy ingeniero'
    def programar(self,lenguaje):
        print 'se programar en: ',lenguaje

class LicenciadoDerecho(Humano):
    def estudiarCaso(self,caso):
        print 'Voy a leer el caso: ',caso

miguel = IngenieroSistemas()
miguel.programar('python')
miguel.saludo('Hola gente')

lila = LicenciadoDerecho(21)
lila.estudiarCaso('del abogado')
print 'tengo',lila.edad
lila.saludo('Mundo')