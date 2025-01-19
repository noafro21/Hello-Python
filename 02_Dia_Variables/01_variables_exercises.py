#Exercises: Level 1
'''Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line'''

# Day 2: 30 Days of python programming
first_name = 'Adonis'
last_name = 'Noa'
full_name = 'Adonis Noa'
country = 'Cuba'
city = 'Guantanamo'
age = 34
year = 1990
is_married = True
is_true = True
is_light_on = True

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Adonis', 'Noa', 'Adonis Noa', 'Cuba', 'Guantanamo', 34, 1990, True, True, True

#Exercises: Level 2
'''Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords'''

print()
print("Se imprime el tipo de dato que representa cada variable")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print()

print("Se imprime la longitud de la variable first_name y last_name")
print(len(first_name))
print(len(last_name))
print() 

# Se declara num_one y num_two
num_one = 5
num_two = 4
print("Se realiza operaciones aritméticas con num_one=5 y num_two=4")
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("La suma de num_one y num_two es: ", total)
print("La resta de num_two y num_one es: ", diff)
print("La multiplicación de num_two y num_one es: ", product)
print("La división de num_one y num_two es: ", division)
print("El módulo de num_two y num_one es: ", remainder)
print("La potencia de num_one elevado a num_two es: ", exp)
print("La división entera de num_one entre num_two es: ", floor_division)
print()

# Se calcula el área y la circunferencia de un círculo 
radius = 30 
PI = 3.14159
area_of_circle = PI * radius ** 2   
circum_of_circle = 2 * PI * radius
print("El área de un círculo con radio de 30 metros es: ", area_of_circle)
print("La circunferencia de un círculo con radio de 30 metros es: ", circum_of_circle)
print()

# Se le solicita que ingrese el radio en metros, para calcular el area de un círculo
radius = input("Ingrese el radio del círculo en metros: ")
area_of_circle = PI * float(radius) ** 2  
print("El área de un círculo con radio de ", radius, "metros es: ", area_of_circle)
print()

first_name = input("Ingrese su nombre")
las_name = input("Ingrese su apellido")
country = input("Ingrese su país")
age = input("Ingrese su edad")

print("Mi nombre completo es:", first_name, last_name, "soy de ", country, "y tengo ", age, "años de edad.")