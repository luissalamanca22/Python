#parar abrir archivos

#el r es de solo escritura y es obligatorio que el archivo exista
# w: escritura. si el archivo no existe crea uno nuevo, si existe, lo escribe
#a: anadir, anade el contenido al final del archivo ya existente
# r+: lectura y escritura. el archivo debe existir

try:
    f = open('ejemplo.txt','w')
except:
    exit()
    print 'Error'

#write solo recive un string
#f.write('Hello ')
#f.seek(-2,2)
#print f.tell()
#f.write('intruso')

#con listas
agregar = ['hola\t', 'mundo\t', 'de programadores']
f.writelines(agregar)
f.close()

#indica si el archivo esta cerrado
if not f.close():
    f.writelines(agregar)

