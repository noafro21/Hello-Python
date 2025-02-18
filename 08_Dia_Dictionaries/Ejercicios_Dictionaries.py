##3Exercises: Day 8 ###
# 1. Create an empty dictionary called dog
perro = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
perro= {'name': 'Martina', 'color': 'Blanco', 'breed': 'Schnauzer', 'legs': 4, 'age': 3}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Adonis', 'last_name': 'Frometa', 'gender': 'M', 'age': 34, 'marital_status': 'Casado', 'skills': ['Python', 'Java', 'CCs', 'JavaScript'], 'country': 'Cuba', 'city': 'Guantánamo', 'address': 'Calle 1ra, # 2, Reparto Centro'}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append( ( 'HTML', 'C++'))
print(student)
print()
# 7. Get the dictionary keys as a list
print(student.keys())
print(perro.keys())
print()
# 8. Get the dictionary values as a list
print(student.values())
print(perro.values())
print()

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())
print(perro.items())
print()

# 10. Delete one of the items in the dictionary.
del student['address']
print(student)

# 11. Delete one of the dictionaries
del perro
# print(perro) # NameError: name 'perro' is not defined