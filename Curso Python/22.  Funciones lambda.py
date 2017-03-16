#funciones lambda:
#   Los lambda siempre me devuleve un valor

li = [1,2,3,-3,-4]
lo = [3,4,5,2,2]
s = "Hola Mundo"

suma = lambda n,m: n+m
print map(suma, li, lo)
print filter(lambda n:n=="o",s)
print reduce(suma, lo)
