lista = [1,2,3,4,-2,-3]
s = ["H","O","L","A"]
l3 = (c * num for c in s
                for num in lista
                    if num > 0)
print lista
#el generador principalmente se usa con tuplas:
# l3 = (c * num for c in s
#                for num in lista
#                    if num > 0)
#el lo que hace es devolver uno por uno de los valores, el generador queda guardado en l3

print l3
print l3.next()
print l3.next()
print '//////////'
for letra in l3:
    print letra

#################################################
#la palabra recervada yield hace referencia que el metodo sea un generador y devuelve un valor
print '//////////'
def factorial(n):
    i = 1
    while n > 0:
        i = n * 2
        yield i
        n -= 1
print 'aqui podemos ver que por yield se convirtio en un genrador: ',factorial(3)
for e in factorial(5):
    print e