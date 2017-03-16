

try:
    f = open('ejemplo.txt','r')
except:
    exit()
    print 'Error'

#read me regresa T_odo el contenido de mi archivo
#hay que tener mucho cuidado si el archivo es demasiado grande puede saturar mi memoria

#print f.read()
#print f.read(10)

#readline va leer linea por linea
#print 'primera linea: ',f.readline()
#print 'nueva linea: ',f.readline()
#print 'tercera linea: ',f.readline()


#while True:
#    print f.read()
#    if f.readline() == '':
#        break

lineas = f.readlines()
for linea in lineas:
    print "=>", linea,"\n\n"