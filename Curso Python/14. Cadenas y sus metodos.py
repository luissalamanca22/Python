s = 'Hola mundo'

#calcular la longitud de la cadena
print len(s)

#Cuantas letras o cadenas hay dentro de mi candena

#count(PalabraBuscar)
print 'Cuantos o hay en ',s,':'
print  s.count('o')

# establecer un inicio y un fin .count(PalabraBuscar, Inicio, Fin)
print 'desde la posicion cero a la posicion 5',':'
print s.count('o',0,5)

#si solo se establece el inicio este va desde le inicio hasta el fina .count(PalabraBuscar,Inicio)
print 'Desde la posicion 6',':'
print s.count('o',6)

#Hacerlo minuscula
print s.lower()

#Hacerlo a mayuscula
print s.upper()

#Cambiar todos los caracteres de mi cadena
print s.replace('o','x')

#.replace(ValorReemplazar, NuevoValor, VecesReemplaza)
print s.replace('o','x',1)

#El metodo split nos devuelve una lista
print s.split('a')

#.split(Separador, LimiteParaSeparar)
print s.split('a',0)

#.find hace la busqueda dentro de la cadena y le da la posicion, sino se encuentra devuelve -1
print s.find('a')
print s.find('o')

#.find buscar
print s.rfind('o')

#recibe ya sea una lista una tupla y un sepearador, en cada uno de los espacios de la tupla le coloca el separador
t = ('H','0','l','a')
s = ';'
print s.join(t)