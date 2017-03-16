#parar abrir archivos

#el r es de solo escritura y es obligatorio que el archivo exista
# w: escritura. si el archivo no existe crea uno nuevo, si existe, lo escribe
#a: anadir, anade el contenido al final del archivo ya existente
# r+: lectura y escritura. el archivo debe existir

#UTILIZANDO r
#try:
#    f = open('ejemplo.txt', 'r')
#except:
#    f='error'
#    print 'error al abrir el archivo'
#print f

f = open('ejemplo.txt','w')
print f
f.close()

