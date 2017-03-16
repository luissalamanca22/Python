#Se crea la clase
class Humano:
    #se crea un metodo por defecto que es el primero que se inicializa, al igual que el parameto self
    def __init__(self, edad):
        #aqui creamos los atributos de la clase
        self.edad = edad

    def saludo(self, mensaje):
        print self.edad,' ',mensaje
        print '////////////////////'

miguel = Humano(21)
miguel.saludo('Hola a todos')
print 'Edad de miguel: ',miguel.edad

lila = Humano(21)
lila.saludo('Mundo')
print 'Edad de lila: ',lila.edad

#OTRO EJEMPLO DE CLASE
class carro:
    def __init__(self):
        self.modelo = ''
    def marca(self,modelo ,descriptcion):
        self.modelo = modelo
        print self.modelo+ ' '+descriptcion

mercedes = carro()
mercedes.marca('mercedes:','carro mas lujoso del mundo')