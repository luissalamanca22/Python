s = ("h","o","l","a","_","c","h","a","o")

def concatenar(a,b):
    print 'valor: ', a
    print 'valor_nuevo: ', b
    print 'se sumo: ',a+b
    return a+b

#reduce es como un acumula el resultado que devuelva va a quedar almacenado
#en la variable a, y el nuevo resultado se asignara a la variable b
sr = reduce(concatenar,s)
print s
print sr

####################################################
def suma(a,b):
    return a+b

n = (1,2,3)
r = reduce(suma,n)
print 'suma de todos los numeros: ',r