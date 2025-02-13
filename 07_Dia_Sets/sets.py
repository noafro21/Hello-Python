### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Adonis", "Noa", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("NoaFro21")

print(my_other_set)  # No se garantiza el orden de los elementos. Un es una estructura ordenada como una lista.

my_other_set.add("NoaFro21")
print(my_other_set)  # No se permiten elementos duplicados. Si se repite un elemento sol se verá reflejado una vez.

my_other_set.update([ "Frometa", "Enfermero", "Cuba" ]) # Agregar varios elementos al set.
print(my_other_set)

print("NoaFro21" in my_other_set)  # Verificar si un elemento está en el set.
print("NoaFro22" in my_other_set)  # Verificar si un elemento está en el set.



my_other_set.remove("NoaFro21")
print(my_other_set)  # Eliminar un elemento del set.

my_other_set.clear()
print(my_other_set)  # Eliminar todos los elementos del set.

print(len(my_other_set))  # Verificar la cantidad de elementos en el set.

del my_other_set
# print(my_other_set)  # Eliminar el set completo.

my_set = {"Adonis", "Noa", 35}
my_list = list(my_set) # Convertir un set en una lista.
print(my_list)  # Convertir un set en una lista.
print(my_list[0])  # Acceder a un elemento de la lista.

my_other_set = {"Java", "Python", "HTML", "CSS", "JavaScript"}

my_new_set = my_set.union(my_other_set)  # Unir dos sets.
print(my_new_set)

print(my_new_set.difference(my_set))  # Diferencia entre dos sets.
