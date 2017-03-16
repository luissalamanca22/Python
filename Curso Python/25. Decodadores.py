#Un decorador es una funcion d que recibe como argumento otra
# funcion a y retorna una nueva funcion b.
# La nueva funcion b es la funcion a decorada con.
#*args -- que recive n cantidades de argumentos
# **kwargs -- este es un diccionario

def decorador(funcion):
    def funcionDecorada(*args,**kwargs):
        print "Funcion Ejecutada", funcion.__name__
        funcion(*args,**kwargs)

    return funcionDecorada

def resta(n,m):
    print n-m


#decorando
resta(5,3)
decorador(resta)(5,3)
#tambien
decorada = decorador(resta)
decorada(3,5)

#como especificar el decorador automaticamente
def decorador1(funcion):
    def funcionDecorada(*args,**kwargs):
        print "Funcion Ejecutada", funcion.__name__
        funcion(*args,**kwargs)

    return funcionDecorada

@decorador1
def resta1(n,m):
    print 'resultado'
    print n-m

resta1(3,5)

#Encadenando docradores
loggeado = True
usuario = 'codigo facilito'

def admin(funcion):
    def comprobar(*args, **kwargs):
        if loggeado:
            print 'esta logeado.'
            funcion(*args, **kwargs)
        else:
            print 'No estas logeado'

    return comprobar

@admin
def algo(usuario):
    print usuario

algo(usuario)

#COn dos decoradores:
# aqui primero ejecuta el ultimo decorador va de abajo hacia arriba
# @admin3
# @decorador3
# cosa que primero ejecuta el decorador3 y despues admin3

login = True
superusuario = 'codigo facilito'

def admin3(funcion):
    def comprobar(*args, **kwargs):
        if login:
            print 'esta logeado.'
            funcion(*args, **kwargs)
        else:
            print 'No estas logeado'

    return comprobar

def decorador3(funcion):
    def comprobar(*args, **kwargs):
        print 'hola'
        funcion(*args, **kwargs)

    return comprobar

@admin3
@decorador3
def cosa(usuario):
    print usuario

cosa(superusuario)