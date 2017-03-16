#una lista puede almacenar cualquier tipo de variable
#bien se tru, false, string, int, etc.

lista1 = [2, "tres", "uno",[3, True]]
l2 = lista1[1]
l3 = lista1[0]
l4 = lista1[3][1]

print 'Esta es la Lista'
print lista1
print '------------------'
print l2
print l3
print l4
print '------------------'
#Los valores en la lista se pueden cambiar dinamicamente
#cambiamos el valor en la pasocion cero
lista1[1] = "cero"
print lista1[1]
print '------------------'

#Crear lista al seleccionar los elementos de otra lista
#el rango es de 0 a 3, el cero indica la posicion del indice que empieza a contrar y el tercero es cuanto quiero contar o copiar#al decir de 0 al 3 coge los elementos en la posicion 0, 1, 2 y deja por fuera el 3
l = lista1[0:3]
print l

#Seleccionar con excepciones
##el rango es de 0 a 3, el cero indica la posicion del indice que empieza a contrar y el tercero es cuanto quiero contar o copiar y va saltaldo de 2 en 2 las excepciones
l = lista1[0:3:2]
print l

#el rango 0:: son todos pero se salta el 2 registro
l= lista1[0::2]
print l

#Reemplazamos varias posiciones o registros
#se reemplaza las tres primera posiciones
lista1[0:3] = ['cero','uno','dos']
print lista1

lista1[0:3] = ['cero']
print lista1

#Recorriendo una lista desde atras
lista2 = [2, "tres", "uno",[3, True]]
l = lista2[-1]
print l
l = lista2[-2]
print l
