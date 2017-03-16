def prueba(f):
    return f()

def porEnviar():
    return 2+2

print prueba(porEnviar)

print '//////////////'

def suma(n,m):
    return n+m

def multiplicacion(n,m):
    return n*m

def seleccion(operacion):
    if operacion == 'suma':
        return suma
    elif operacion =='multi':
        return multiplicacion

resultado = seleccion('suma')(2,3)
print resultado
resultado = seleccion('multi')(2,3)
print resultado

#tambien se puede usar de esta forma
resultado = seleccion('suma')
print resultado(2,4)