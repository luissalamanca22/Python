#las excepciones aparecen cuando ocurre un error

print 'bienvenido'
#como se controla los errores
try:
    print l
except:
    print 'error de ejecucion'

#controlando los errores por los tipos de errores
try:
    print 1/0
except (TypeError,NameError):
    print 'error de ejecucion'
except ZeroDivisionError:
    print 'No se puede dividir entre cero'

#
try:
    print l
except (TypeError,NameError):
    print 'error de ejecucion'
except ZeroDivisionError:
    print 'No se puede dividir entre cero'

#
i = 8
try:
    print i/8
except (TypeError,NameError):
    print 'error de ejecucion'
except ZeroDivisionError:
    print 'No se puede dividir entre cero'
else:
    print 'No hubo error'

#finally se ejecuta haya o no haya un error
#
i = 8
try:
    print i/8
except (TypeError,NameError):
    print 'error de ejecucion'
except ZeroDivisionError:
    print 'No se puede dividir entre cero'
else:
    print 'No hubo error'
finally:
    print 'No hubo errores'


print 'Adios'
