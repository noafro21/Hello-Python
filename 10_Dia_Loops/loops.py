### Loops ###

#While Loop
count = 0
while count <5:
    print(count)
    count = count + 1
print("")
#prints from 0 to 4

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
print("")
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
print("--------------------")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5  

print("Bucle for con cadena")
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

print("Bucle for con tupla")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print("Bucle con diccionario Al recorrer un diccionario se obtiene la clave del diccionario.")
person = {
    'first_name': 'Adonis',
    'last_name': 'Noa',
    'age': 34,
    'country': 'Costa Rica',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'}
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

print("Bucle con conjunto")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company) # this way we get all the companies printed out

print("Romper y continuar - Parte 2")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


#La función de rango
print("La función de rango")
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# syntax
#for iterator in range(start, end, step):
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

#Bucle For anidado
print("Bucle For anidado")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#Si queremos ejecutar algún mensaje cuando finaliza el bucle, utilizamos else.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

"""Aprobar
En Python, cuando se requiere una declaración (después del punto y coma), pero no queremos ejecutar ningún código allí, podemos escribir la palabra pass para evitar errores. También podemos usarla como un marcador de posición para declaraciones futuras."""
print("Pass")
for number in range(6):
    pass