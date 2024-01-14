#iterando una LISTA// funciona igual para TUPLAS y CONJUNTOS
animales = ["gato","perro","loro","cocodrilo"]
numeros = [1,2,3,4,5,6,7] #lista
numeros= {1,2,3,4,5,6,7} #conjunto

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es: {animal}')

#recorriendo la lista numeros
for numero in numeros:
    resultado = numero*10
    print(f'Ahora la variable resultado es : {resultado}')

#recorriendo ambas listas  a la vez
for animal,numero in zip(animales,numeros):
    print(f'Recorriendo Animales : {animal}')
    print(f'Recorriendo Numeros : {numero}')

#forma correcta de iterar una lista con su indice
for num in enumerate(numeros):
    print(num)
    indice = num[0]
    valor = num[1]
    print(f'El indeice es :{indice} y el valor es :{valor}')


#iterando un DICCIONARIO    
diccionario = {
    "nombre" : "Mauro",
    "Apellido" : "Montaño",
    "Carrera" : "Ing.Informatica"
}
#itero e imprimo solo las keys
for key in diccionario:
    print(key)

#iterando las keys con los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La calve es :{key} y el valor es :{value}')