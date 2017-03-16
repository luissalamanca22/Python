lista = [1,'Dos',3]
buscar = 1

#buscar en una palabra en una lista
valor = buscar in lista
print 'EL numero ',buscar,' esta: ',valor

#coger el index o posicion de uan palabra en una lista, sino lo encuentra arroja un error por lo tanto hacemos el
#procedimiento de abajo
print lista.index(buscar)

#
if buscar in lista:
    print 'Posicion de la letra: ',lista.index(buscar)
else:
    print 'No esta en la lista'

#Agregando un nuevo elemento a la lista
print 'lista vieja: ',lista
lista.append('cuatro')
print 'Lista nueva: ',lista

#SABER CUANTAS VECES SE REPITE UN ELEMENTO DENTRO DE UNA LISTA
print lista.count(1)

#Reemplazar o insertar en una posicion un registro
#.insert(posicion, value)
lista.insert(1, 'vidas')
print lista

#
iterable = 'cinco'
lista.extend(iterable)
print lista

#tambien se puede agregar una lista
iterable = [1,2,3,4]
lista.extend(iterable)
print lista

# extraer y borrar un elemento de unalista
#.pop(IndiceElementoBorrar)
lista.pop(1)
print lista

#Elemento que quiero borrar, este solo borra una vez como asi si hay dos o entonces solo borra una
#.remove(ElementoBorrar)
lista.remove(1)
print lista

#Ivertir los elementos de una lista
lista.reverse()
print lista