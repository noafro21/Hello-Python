#Ejercicios: Día 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
#1. Find the length of the set it_companies
print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["TikTok", "Snapchat", "Linkedin"])
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove("Apple")
print(it_companies)
#5. What is the difference between remove and discard

#Exercises: Level 2
#1. Join A and B
AB = A.union(B)
print(AB)

#2. Find A intersection B
print(A.intersection(B))
print(B.intersection(A))

#3. Is A subset of B
print(A.issubset(B))

#4. Are A and B disjoint sets?
print(A.isdisjoint(B))

#5. Join A with B and B with A
print(A.union(B))  
print(B.union(A))    

#6. What is the symmetric difference between A and B?
print(A.symmetric_difference(B))

#7. Delete the sets completely
del A
del B

#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
conjunto_age = set(age)
print(len(age))
print(len(conjunto_age))
print(len(age) > len(conjunto_age)) # La lista (age) es más grande que el conjunto (conjumto_age).

#2. Explain the difference between the following data types: string, list, tuple and set
# Cadena ==> Es una secuencia de caracteres que se puede acceder mediante índices. Es inmutable.
# Lista ==> Es una secuencia de elementos que se pueden acceder mediante índices. Es mutable.
# Tupla==> Es una secuencia de elementos que se pueden acceder mediante índices. Es inmutable.
# Conjunto ==> Es una colección de elementos únicos y no ordenados. Que no permite elementos duplicados.

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.