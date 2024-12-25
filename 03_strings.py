# Strings. Cadenas de texto. 
my_string= 'Mi String'
my_other_string= 'Mi otro String'

print(len(my_string)) 
print(len(my_other_string))
print(my_string+" "+my_other_string)

my_new_line_string = 'Esto es un estring\ncon salto de línea'
print(my_new_line_string)

my_tab_line_string = '\tEsto es un estring con salto de línea\ny con tabulación'
print(my_tab_line_string)

### Formateo de cadena (% y str.format)

name, surname, age = "Adonis", "Noa", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #
print("Mi nombre es",name, surname,"y mi edad es",age)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Indexación y segmentación de cadenas

languaje = "Python"
a,b,c,d,e,f = languaje
print(a,b,c,d,e,f)



languaje_slice = languaje[1:6] # Se especifica el rango de caracteres que queremos obtener
print (languaje_slice)
languaje_slice = languaje [1:3] 
print (languaje_slice)
languaje_slice = languaje [0:6:2] # Se especifica el rango de caracteres que queremos obtener y el salto
print (languaje_slice)
languaje_slice = languaje [::-1] # Se invierte el string
print (languaje_slice)


# Métodos de cadena
print(languaje.capitalize()) # Convierte la primera letra en mayúscula
print(languaje.upper())      # Convierte todas las letras en mayúscula
print(languaje.lower())      # Convierte todas las letras en minúscula
print(languaje.replace("P", "J")) # Reemplaza una letra por otra
print(languaje.count("t")) # Cuenta cuantas veces aparece una letra
print(languaje.startswith("P")) # Devuelve True si la cadena empieza con la letra especificada
print(languaje.endswith("n")) # Devuelve True si la cadena termina con la letra especificada
print(languaje.split("t")) # Divide la cadena en una lista de subcadenas
print(languaje.find("t")) # Devuelve la posición de la primera aparición de la letra especificada
print(languaje.index("t")) # Devuelve la posición de la primera aparición de la letra especificada
print(languaje.isnumeric()) # Devuelve True si la cadena es numérica
print(languaje.isalpha()) # Devuelve True si la cadena es alfabética
print(languaje.isalnum()) # Devuelve True si la cadena es alfanumérica 
print(languaje.isspace()) # Devuelve True si la cadena contiene solo espacios en blanco
print(languaje.isupper()) # Devuelve True si la cadena está en mayúsculas
print(languaje.islower()) # Devuelve True si la cadena está en minúsculas
print(languaje.istitle()) # Devuelve True si la cadena está en formato de título
print(languaje.strip()) # Elimina los espacios en blanco al principio y al final de la cadena
print(languaje.lstrip()) # Elimina los espacios en blanco al principio de la cadena
print(languaje.rstrip()) # Elimina los espacios en blanco al final de la cadena
print(languaje.center(10)) # Centra la cadena en un ancho de 10 caracteres
print(languaje.ljust(10)) # Justifica a la izquierda la cadena en un ancho de 10 caracteres
print(languaje.rjust(10)) # Justifica a la derecha la cadena en un ancho de 10 caracteres
print(languaje.zfill(10)) # Rellena la cadena con ceros a la izquierda en un ancho de 10 caracteres
print(languaje.join("123")) # Une los elementos de una cadena con la cadena especificada
print(languaje.partition("t")) # Divide la cadena en una tupla con tres elementos
print(languaje.rpartition("t")) # Divide la cadena en una tupla con tres elementos
print(languaje.lower().isupper()) # Encadenamiento de métodos (debe devolver True o False en cado que se cumpla o no la condición)
print(languaje.startswith("py")) # Encadenamiento de métodos (debe devolver True o False en cado que se cumpla o no la condición)



