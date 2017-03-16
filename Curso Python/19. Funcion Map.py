def operador(n,m):
    if n==None or m==None:
        return 0
    else:
        return n + m

lista = [2,3,4,5]
tupla = (6,7,8,9)

#El map lo que hace es recorrer y colocar
# cada uno de los elemento q hay en la
#lista y tupla en el metodo operador y despues como resultado obtenemos
#una lista

lista_respuesta = map(operador,lista,tupla)

#que pasa si las dimensiones no coinciden entre tupla y lista, el que
#tenga la menor dimension se agregara none hasta quede de igual
#que la otra lista o tupla
tupla2 = (6,7,8)
lista_respuesta2 = map(operador,lista,tupla2)

#tambien lo podemos hacer con cadenas
s1 = "Hola"
s2 = "Mundo"

lista_respuesta3 = map(operador,s1,s2)

print lista_respuesta
print lista_respuesta2
print lista_respuesta3