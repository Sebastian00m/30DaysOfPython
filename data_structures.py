"""Si deseamos crear culaquier estructura de datos vacia 
debemos usar sus respectivas funciones(dict(),list(),tuple(),set()), y no de otra forma"""
#TUPLAS

#creando tuplas con valores
tupla = tuple(["dato 1", "dato 2"])
#ambos funcionan de la misma manera
tupla = "dato 1", "dato 2"

#creando una tupla con un unico valor
tupla = "dato 1",

print(tupla)


#SETS(Conjuntos)  // los conjuntos no son modificables
#creando un conjunto con set()
conjunto = set(["dato 1", "dato 2"])

#conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificar si es subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2<=conjunto1

#verificar si es superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verificar si hay algun valor en comun
resultado = conjunto1.isdisjoint(conjunto2) 
"""retorna True solo cuando los conjuntos que se estan comparando 
no tienen ningun numero en comun"""

print(resultado)


#DICCIONARIOS

#creando diccionariois con dic()
diccionario = dict(nombre='mauro',apellido='Montaño')

#las listas no pueden ser claves y usameos frozenset para meter conjuntos
diccionario = {frozenset(["Mauro","Dev"]):"2024"}

#crear un diccionario con claves pero sin valores, con valores none
diccionario = dict.fromkeys(["Nombre","Apellido","carrera"])
diccionario = dict.fromkeys("ABCDE")
diccionario = dict.fromkeys("ABCDE","Puto")#divide el primer parametro para crear las keys y les asigna el valor del segundo parametro
diccionario = dict.fromkeys(["Nombre","Apellido"],"puto") 

print(diccionario)