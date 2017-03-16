#WHILE
i = 0
while i < 5:
    i+=1
    print i

#cuando el bucle detecta continue ignora_todo lo que sigue despues
print "////////////////"
i = 0
while i < 10:
    if i == 5:
        i+=1
        continue
    print i
    i+=1

#cuando se usa el break se rompe el ciclo
print "////////////7"
i = 0
while i < 10:
    if i == 5:
        break
    print i
    i+=1

#FOR IN
#este recorre listas, tuplas y diccionarios
listas = ['elementos1', 'elementos2', 'elementos3']
print '////////////'
for lista in listas:
    print lista

#tambien se puede hacer con una cadena
print '////////////'
for letra in 'medico':
    print letra
