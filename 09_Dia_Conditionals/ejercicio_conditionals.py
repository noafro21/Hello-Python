#Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

'''age = int(input('Ingrese su edad actual: '))
if age >= 18:
    print ("Tienes ",  age,  " años, edad suficiente para manejar.")
else:
    print ("Te faltan ", 18-age , " años para poder manejar")'''
    
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

'''you_age = 40

my_age = int (input("Igresa tu edad actual "))
if my_age > you_age:
    print ("Tu edad es mayor que mi edad, tienes ", my_age - you_age, " años más que yo.")
elif my_age < you_age:
    print ("Tu edad es menor que la mia, eres ", you_age-my_age, " años menor que yo.")  
else: 
    print ("Mi edad es igual a la tuya, tienes ", my_age, " años")'''
    

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

'''a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
if a > b:
    print ("{} es mayor que {}" .format(a,b))
elif a < b:
    print ("{} es menor que {}" .format(a,b))
else:
    print ("{} es igual a {}" .format(a,b))'''
        
#Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:

'''90-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''
'''note = float((input("Ingreese la nota del estudiante: ")))
if note <=49:
    print("El estudiante obtuvo la calificacion  'F'")
elif note <= 59:
    print("El estudiante obtuvo la calificacion  'D'")
elif note <= 69:
    print("El estudiante obtuvo la calificacion  'C'")
elif note <= 89:
    print("El estudiante obtuvo la calificacion  'B'")
elif note <= 100:
    print("El estudiante obtuvo la calificacion  'A'")
else:
    print("Ingrese una calificacion valida")'''
        

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# Creo 3 tuples que contienen los meses que identifica a cada estación.
autumn = ('Septiembre','Octubre', 'Noviembre')
winter = ('Diciembre', 'Enero', 'Febrero')
sprint = ('Marzo', 'Abril','Mayo')
summer = ('Junio', 'Julio', 'Agosto')

'''month = str.capitalize(input("Para comprobar la estación del año ingrese el nombre del mes: "))

if month in autumn:
    print ("La estacion del año es otoño")
elif month in winter:
    print ("La estacion del año es invierno ")
elif month in sprint:
    print ("La estacion del año es primavera")
elif month in summer:
    print ("La estacion del año es verano")
else:
    print("Ingrese un mes válido")'''
    
# 3. La siguiente lista contiene algunas frutas:

'''fruits = ['banana', 'orange', 'mango', 'lemon']

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.

look_for_fruit = str.lower(input("Ingrese el nombre de la fruta que desea buscar: "))
if look_for_fruit in fruits:
    print ("La fruta está en la lista")    
else:
    print ("La fruta no esta en la lista, se va a agregar")
    fruits.append(look_for_fruit)
    print ("Lista actualizada: ",fruits)'''
    
    #Ejercicios: Nivel 3
#Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!
person={
    'first_name': 'Adonis',
    'last_name': 'Noa',
    'age': 34,
    'country': 'Costa Rica',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print ('skills' in person)
print(person['skills'][2])

#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

print ('skills' in person)
print(person ['skills']['Python'])

#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

#* If the person is married and if he lives in Finland, print the information in the following format:
