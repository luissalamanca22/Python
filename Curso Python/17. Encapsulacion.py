#La encapsulacion se trata de establecer metodos o variables privadas
#y propinarles un valor

#cuando se colocan los dos guiones raya al piso es porque se esta especificando que es privado as :
# __nombre, la variable nombre es privada

#RECUERDA: que las variables privadas se pueden llamar dentro de la clase

class Prueba(object):
    def __init__(self):
        self.__privado = 'soy privado'
        self.publico = 'soy publico'

    def __metodoPrivado(self):
        return 'Soy un metodo privado'

    def metodoPublico(self):
        return 'Soy un metodo publico'

    #Capturando dato a la variable privada '__privado'
    def getPrivado(self):
        return self.__privado

    def setPrivado(self, saludo):
        #self.__privado = saludo
        self.__privado = self.__metodoPrivado()+' '+saludo

obj = Prueba()
print obj.publico
obj.publico = 'cambie el valor de publico'
print obj.publico
print obj.metodoPublico()
print obj.getPrivado()
#obj.setPrivado('Cambie el valor de la variable privada')
obj.setPrivado('saludo')
print obj.getPrivado()

