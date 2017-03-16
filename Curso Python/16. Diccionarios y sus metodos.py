# -*- coding: utf-8 -*-
diccionario = {
    "redes_sociales" : ['twitter', 'facebook','Linkedin'],
    3:'tres',
    'Hola':'mundo'
}




#para ver si tiene un clave o no
print 'Diccionario: '
print diccionario
print '¿La clave Hola esta en el diccionario?: '
print diccionario.has_key('Hola')
print '¿La clave 4 existe en el diccionario?:'
print diccionario.has_key(4)

#de un diccionario devuelvame una tupla
print 'Convierte el diccionario en una tupla'
print diccionario.items()

#nos devuelve una lista con todas las clves del diccionario
print 'nos devuelve una lista con todas las clves del diccionario'
print diccionario.keys()

#me devuelve los valores de un diccionario mas no las claves
print 'me devuelve los valores de un diccionario mas no las claves'
print diccionario.values()

#se borra la clave con su valor q se especifica .pop(clave, ValorQueDevuelve) y si no se encuentra ese valor que se busca devuelve
#en la variable ValorQueDevuelve que es un valor por defecto que nosotro asignamos para que nos devuelva sino se encuentra nada
print 'se borra la clave con su valor q se especifica .pop(clave, diccionario), ademas de:'
print diccionario.pop(3,'No se encontro')
print diccionario.pop(10,'No se encontro')


#Si quiero eliminar un elemento dentro de mi diccionario
print diccionario
del diccionario['Hola']
print diccionario

#eliminar todos los elementos de diccionario
print 'limpiar mi diccionario'
print diccionario
diccionario.clear()
print diccionario

#Agregar datos a mi diccionario
diccionario['clave'] = 'la van van'
print diccionario

#Copiar el diccionario a diccionario2
diccionario2 = diccionario.copy()
print 'Copiando del diccionario a diccionario2'
print  diccionario
print diccionario2
