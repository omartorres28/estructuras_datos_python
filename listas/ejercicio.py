# Ejercicios listas

# Ejercicios manipulacion


# 1.Consiste en la deficion de una lista con elementos de diferentes tipos y en mostrarla por pantalla,tanto entera como por elementsoaceddiendo a la posicion que ocupa dentro de la lista 

lista = [ "Python", "Guanenta" ,2022,"libro", 3]
print(lista)
print(lista[0])
print(lista[2])

#2. consiste en el uso del operador + para realizar uniones de listas.
lista1 = ["camiseta","Pantalon","Zapatillas"]
lista2 = ["Abrigo","Jersey", "Sudadera", "Calcetines"]
print("Numero elemento lista1: "  , len(lista1))
print("lista1: ", lista1)
print("Numero elemento lista2: " , len(lista2))
print("lista2: ", lista2)
lista_concatenada = lista1 +lista2
print("Numero elemnto lista_contatenada: " , len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

#3.Añadir elementos de diferentes formas 
lista = ["camiseta","Pantalon","Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey","Sudadeda"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)

#4.Modificar elementos de una lista y borrar elementos de la misma
lista = ["camiseta","Pantalon","Zapatillas"]
print(lista)
lista[1] ="Cazador"
print(lista)
del lista[0]
print(lista)

#5.Uso del operador*. que permite concatenar una lista con ella misma un numero finito de veces.
lista = (lista)
print(lista)
lista_resultante = lista * 3
print(lista_resultante)


#6. creacion de listas como elementos de listas y acceso a dichos elementos.

print("---Ejercicio 6---")
lista = ["Camiseta",["Calcetines","cazadores"],"Zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])



#7. Extraer una porcion de la lista en una lista nueva.

print("---Ejercicio 7---")
lista=[1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 =lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)