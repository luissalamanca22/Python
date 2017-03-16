#La compresion de listas viene a reemplazar a
#filter, map

lista = [1,2,3,4,-2,-3]
s = ["H","O","L","A"]
#hay dos variables num, la de la izquierda y la de la derecha
#el recorre la lista y guarda el valor en la variable num de la derecha
#si la condicion se cumple lo guarda en la variable num de la izquierda
l2 = [num for num in lista if num>0]
l3 = [c * num for c in s
                for num in lista
                    if num > 0]
print lista
print l2
print '/////////////'
print lista
print l3