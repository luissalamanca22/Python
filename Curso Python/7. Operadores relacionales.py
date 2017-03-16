#me permite comparar dos elementos o mas elementos y me devuelve un true o un false
# si 5 es igual a 4, obvio que no lo son por lo tanto me devuelve un false
r = 5 == 4
print '1'
print r

r = 5 != 4
print '2'
print r

r = 5 > 4
print '3'
print r

r = 5 < 4
print '4'
print r

r = 5 >= 4
print '5'
print r

r = 5 <= 4
print '6'
print r

#tambien se puede hacer para los string
r = 'hola' == 'hi'
print '7'
print r

#tambien podemos compara con listas, tuplas y diccionarios: false
r = ['hola', 3 , 4] == ['hi',3, 2 ]
print '8'
print r

#este da true
v = ['hola',3,4]
c = ['hola',3,4]
r = v == c
print '9'
print r

