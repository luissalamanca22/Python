#FUNCIONES

#se declara la funcion
def mi_funcion(num1,num2):
    print num1 + num2
#se llama la funcion
mi_funcion(5,6)


#Definir valores por defecto
    #si los parametros de la funcion estan igualdos a un valor, este valor seria el valor por defecto
    #el valor por defecto se le otorga a la variable cuando no se le envia un o todos los parametros a la funcion
print '////////////'
def mi_funcion_2(num1 = 1, num2 = 0):
    print num1 + num2

mi_funcion_2()

#con cadenas
print '////////////'
def mi_funcion3(cadena,repeticion = 3):
    print cadena * repeticion
mi_funcion3('ola',5)

#N parametos
    #al especificar *N_parametros se recibe n parametos, en N_parametros los parametos de mas se van a guardar como una tupla
print '////////////'
def mi_funcion4(cadena, repeticion =3, *N_parametros):
    print  cadena * repeticion
    for n in N_parametros:
        print n
mi_funcion4('ola',4,'Hola','como','esta', 'mundo')

#N parametos
    #al especificar **N_parametros se recibe n parametos, en N_parametros los parametos de mas se van a guardar como un diccionario
print '//////////////////////'
def mi_funcion5(cadena, repeticion =3, **N_parametros):
    print  cadena * repeticion
    print N_parametros['saludo']
mi_funcion5('ola',4,saludo = 'mundo')


#REGRESAR UN VALOR
print '//////////////////////'
def mi_funcion6(num1,num2):
    return num1 + num2
resultado = mi_funcion6(4,3)
print resultado