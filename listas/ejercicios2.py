# Ejercicios listas

# Ejercicios manipulacion

lista = [45, 32,3,78]
print("lista original: ", lista)
# Funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append: ", lista)
# Funcion sort: ordene la lista 
lista.sort()
print("Lista ordenada ", lista)
# Funcion reverse: invierte el orden de la lista 
lista.reverse()
print("Lista al reves: ", lista)
# Funcion extend: añade los elementos de una lista a lista 
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("lista despues de extend: ", lista)
# Funcion count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista
print(" Numero de elemntos 45: ", lista.count(45))
# Funcion insert: añade ele elemento pasado como parametro a la lista en la posicion tambien parametro
lista.insert(4,111)
print("Lista despues de insert. ", lista)
# Funcion remove: elimina la primera ocurrencia empezando por la izquierda de la lista del elemnto indicado como parametro.
lista.remove(45)
print("Lista despues de remove: ", lista)
# Funcion index: devuleve la posicion de lamprimera ocurrencia de la derecha en la lista, del elemento pasado como parametro.
print("Posicion del elemento 111: ",lista.index(111))
# Funcion pop: Elimina un eloemen to de la lista y lo devulve como resultado de la operacion.
lista.pop()
print("Lista despues de pop: ", lista)
# Funcion clear: elimina todos los elementos de la lista
lista.clear()
print("Lista despues de clear: ", lista)