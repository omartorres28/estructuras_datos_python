#Ejercicios tuplas

# Métodos propios.

# 1. Funcion cound: cuenta el numero de veces que apparece el elemento indicado como parámetro dentro de tupla.
tupla = ("Casa", "2", 99 ,  345, "Perro", 99)
print("Elemntos de la tupla: ", tupla)
print("Numero de elementos 99: ",tupla.count(99))

# 2. Funcion index: Devuelve la posicion de la primera ocurrencia de izquierda a dereca en la tupla del elemento pasado como parametro
tupla = ("Casa", "2", 99 ,  345, "Perro", 99)
print("Elemntos de la tupla: ", tupla)
print("Posicion que ocupa el elemento Perro: ",tupla.index("Perro"))