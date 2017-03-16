def filtro(elemento):
    return (elemento>0)

#como resultado me devuelve una lista
lista = [1,2,4,5,-10,-2,-4]
lista_resultado = filter(filtro,lista)
print lista
print lista_resultado

##########################################
def filtro2(elemento):
    return (elemento == "o")

s = "Hola mundo"
#como resultado me devuelve un string
lista_resultado2 = filter(filtro2,s)
print s
print lista_resultado2