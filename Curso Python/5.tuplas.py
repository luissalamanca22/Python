# Los datos de las tuplas no se pueden modificar, ni agregar mas elementos
t = ("hola", "hello", 'hi')
print t
print type(t)
#acceder a los elementos de una tupla
print t[1]

#tambien se puede una tupla dentro de otra tupla
t2 = (("hola","hi"), "hello")
print "////////"
for t in t2:
    print t
