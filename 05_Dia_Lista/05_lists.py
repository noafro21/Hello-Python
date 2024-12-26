### Lists ###

my_list = list() # Crear una lista vacía
my_other_list = [1,2,3,4,5] # Crear una lista con valores
print(my_other_list)
print(my_list)
print(type(my_list))
print(len(my_other_list))
my_list= [35,34,30,30,25,28,40] # Crear una lista con valores
print(my_list)
print(len(my_list))

my_other_list = [34,1.75, 'Adonis', 'Noa'] # Lista con diferentes tipos de datos
print(type(my_other_list)) # Imprimir el tipo de dato de la lista
print(my_other_list) # Imprimir la lista

# Acceder a los elementos de una lista

print(my_other_list[0]) # Imprimir el primer elemento de la lista
print(my_other_list[1]) # Imprimir el segundo elemento de la lista
print(my_other_list[2]) # Imprimir el tercer elemento de la lista
print(my_other_list[-1]) #  Imprimir el último elemento de la lista
print(my_other_list[-2]) # Imprimir el penúltimo elemento de la lista
print(my_other_list.count("Adonis"))   # Contar cuantas veces se repite un elemento en la lista
print(my_other_list.index("Noa")) # Encontrar el índice de un elemento en la

age, height, name, surname = my_other_list # Asignar los valores de una lista a variables
print(age)

print(my_other_list + my_list) # Concatenar dos listas
#prin(my_other_list - my_list) # Restar dos listas no se puede hacer
print(my_other_list, my_list)  # Imprimir dos listas


print("Se agrega un elemento al final de la lista")
my_other_list.append("Noafro") # Agregar un elemento al final de la lista
print(my_other_list)
print()
print("Se inserta un elemento en una posición(4) específica de la lista")
my_other_list.insert(4,"Prometa") # Agregar un elemento en una posición específica
print(my_other_list)

my_other_list[4] = "Frometa" # Agregar un elemento en una posición específica
print(my_other_list)

print()
print("Se remueve un elemento(Noafro) deseado de la lista")
my_other_list.remove("Noafro") # Eliminar un elemento de la lista
print(my_other_list)

my_list.remove(30)
print(my_list)


my_list.pop()   # Eliminar el último elemento de la lista
print(my_list)

print(my_list.pop()) # Eliminar el último elemento de la lista y retornarlo
print(my_list)

my_pop_element = my_list.pop(2) # Eliminar un elemento de la lista y retornarlo
print(my_pop_element) # Eliminar el último elemento de la lista y retornarlo
print(my_list)

del my_list[1] # Eliminar un elemento de la lista
print(my_list)
my_new_list = my_list.copy() # Copiar una lista
my_list.clear() # Eliminar todos los elementos de la lista

my_new_list.reverse() # Invertir la lista
print(my_new_list) # Imprimir la lista invertida

my_new_list.sort() # Ordenar la lista
print(my_new_list) # Imprimir la lista ordenada

print(my_list)
print(my_new_list)

my_list = "Hola Python" # Crear una lista con un string
print(my_list)
print(type(my_list))