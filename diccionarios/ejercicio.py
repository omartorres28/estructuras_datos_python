# Ejercicios Diccionarios


# Manipulacion

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday",}

print(diassemanaingles["Lunes"])
print(diassemanaingles["Miércoles"])
print(diassemanaingles["Viernes"])

#  Añade los días sábado y domingo, modificando el valor de algún elemento y borrando algún elemento.

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print(diassemanaingles)
diassemanaingles["Sábado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

# ejercicio 3. Es posible utilizar las funciones len, max y min con los diccionarios. La primera devolverá el número de elementos que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor seran devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario.

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print("Número de elementos del diccionario: ", len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))

# Ejercicio 4. ejecucion 

diassemanaingles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday",
                    "Miércoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}
                    
print("Diccionario original: " , diassemanaingles)

# Función Copy: Realiza una copia exacta del diccionario en uno nuevo. 
diccionariocopia = diassemanaingles.copy()
print("Diccionario copia: " , diccionariocopia)

# Función Pop: Obtiene el valor de la clave pasada como parámetro y además elimina el elemento del diccionario.
print("Valor del Lunes (Pop): " , diassemanaingles.pop("Lunes"))
print("Diccionario después del pop: " , diassemanaingles)

# Función Popitem: Obtiene un elemento aleatorio del diccionario y lo elimina del mismo.    
print("Elemento al azar con  popitem: " , diassemanaingles.popitem())
print("Diccionarios después de Popitem: " , diassemanaingles)

# Función get: Obtiene el valor de la clave pasada como parámetro.
print("Valor del Martes (Get): " , diassemanaingles.get("Martes"))
print("Valor del Lunes (Get) ( no existe): " , diassemanaingles.get("Lunes"))
print("Valor del Lunes (Get) ( no existe): " , diassemanaingles.get("Lunes" , "No existe"))

# Función Update: Actualiza el diccionario utilizando otro diccionario. 
diassemanaingles.update({"Lunes": "MondayNUEVO", "Martes": "TuesdayNUEVO"})
print("Diccionario después del update: " , diassemanaingles)

# Función Setdefault: Intena insetar un elemento (clave y valor) en el diccionario. En caso de no  existir dicho elemento. la función inserta y devuelve el valor del elemento y en caso de existir, lo único que hace es devolver el valor actual.
print("Setdefault: " , diassemanaingles.setdefault("Sabado" , "Saturday"))
print("Diccionario después del setdefault (Nuevo Elemento): " , diassemanaingles)
print("Setdefault del Lunes: " , diassemanaingles.setdefault("Lunes" , "Lunes"))
print("Diccionario después del setdefault (Elemento existente): " , diassemanaingles)

# Función Items: Devuelve un objeto iteravle (que puede utilizarse en bucles).
print("Elemento iterable (Items): " , diassemanaingles.items())

# Función Keys: Devuelve un objeto iteravle (que puede utilizarse en bucles) con las claves del diccionario.
print("Elemento iterable (Claves): " , diassemanaingles.keys())

# Función Values: Devuelve un objeto iteravle (que puede utilizarse en bucles) con los valores del diccionario.
print("Elemento iterable (Valores): " , diassemanaingles.values())

# Función Clear: Elimina todos los elementos .
print("Diccionario antes del clear: " , diassemanaingles)
print("Diccionario después del clear: " , diassemanaingles.clear())