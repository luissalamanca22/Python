#comillas simples
cads = 'Texto entre comillas simples'

#salto de linea
#Salto de linea es \n y el tap o espacio es \t
cads1 = 'Texto entre \n comillas simples'
cads2 = 'Texto entre \n\t comillas simples'
cads3 = ''' Texto linea 1
linea2
linea3
linea4
.
.
'''
print cads1
print '//////////'
print cads2
print '//////////'
print cads3

#Comillas dobles
cadd = "Texto entre comillas doble"

#vemos el tipo de la variable: si sale str significa que es strig
print '//////////'
print type(cads)
print type(cadd)

#REPETICION
print '//////////'
cad = 'cadena' * 3
print cad

#CONCATENACION
cadena1 = 'cadena1'
cadena2 = ' cadena2'
print '//////////'
print cadena1 + cadena2

#Boleanos
bT = True
bF = False

#OPERADORES LOGICOS
#and: devuelve tru cuando todos son true
bAnd = True and False
print  bAnd
#or: con un true devuelve true
bOr = True or False
print bOr
#not True: lo convierte en false y viceversa
bNot = not True
print bNot
