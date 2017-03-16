#recibir valores desde el teclado

valor = raw_input("Introduce un numero entero: ")

try:
    valor = int(valor)
except:
    print 'Eso no es un valor'
else:
    print 'si es un numero entero'
    print valor