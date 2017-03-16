class Decorador(object):
    """mi Clase decoradora"""
    def __init__(self,funcion):
        self.funcion = funcion
    #este fucion va hacer, la funcion comprobar como se venia manejando en el archivo decoradores.py
    def __call__(self, *args, **kwargs):
        print "funcion ejecutada", self.funcion.__name__
        self.funcion(*args,**kwargs)

@Decorador
def resta(n,m):
    print n-m

resta(3,5)