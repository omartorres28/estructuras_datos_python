# Ejercicio tuplas

# Cadenas de textos

tupla = ("Casa", "2", 345, "Perro", 99)
print("Elementos de la tupla: ", tupla)
print("Elemento de la poscion 0: ", tupla[0])
print("Elemento de la posicion 1 ", tupla[1])
print("Elemento de la posicion 1 ", tupla[2])
print("Elemento de la posicion 1 ", tupla[3])
print("Elemento de la posicion 1 ", tupla[4])

# 1. Funcion cound: cuenta el numero de veces que apparece el elemento indicado como parámetro dentro de la tupla.
tupla = ("Casa", "2", 99 ,  345, "Perro", 99)
print("Elemntos de la tupla: ", tupla)
print("Numero de elementos 99: ",tupla.count(99))

# 2. Funcion index: Devuelve la posicion de la primera ocurrencia de izquierda a dereca en la tupla del elemento pasado como parametro.
tupla = ("Casa", "2", 99 ,  345, "Perro", 99)
print("Elemntos de la tupla: ", tupla)
print("Posicion que ocupa el elemento Perro: ",tupla.index("Perro"))

# 3. Extraer posiciones de la tupla en una tupla nueva.
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

# 4. Consiste en el uso de operador + para realizar uniones de listas. Además utilizar la función len para conocer el numero de elementos que componen la lista.

tupla1 = (2, "television",8763)
tupla2 = (1,2,3, "Videojuego")
print("Numero elementos de tupla1: ",len(tupla1))
print("tupla1: ", tupla1)
print("Numero elementos de tupla2: ", len(tupla2))
print("tupla2: ",tupla2)
tuplaconcatenada = tupla1 + tupla2
print("Numero elementos de tuplaconcaenada: ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

# 5. Uso del operedor * que permite concatenar una tupla con ella misma un número finito de veces.
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)
