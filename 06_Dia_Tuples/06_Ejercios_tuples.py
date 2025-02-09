#Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = tuple()
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_tuples_sisters = ('Elianis','Juliana', 'Gloriana')
my_tuples_broders = ('Alexander', 'René', 'Alberto','Armando')
print(my_tuples_sisters)
print(my_tuples_broders)
#3. Join brothers and sisters tuples and assign it to siblings
tuples_siblings = my_tuples_sisters + my_tuples_broders
print(tuples_siblings)

# 4. How many siblings do you have?
print(len(tuples_siblings))
      
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tuples_siblings + ('Nireldi', 'Taiza')
print(family_members)

#Exercises: Level 2

# 1. Unpack siblings and parents from family_members


# 2. Create fruits, vegetables and animal products tuples.
fruit = ('mango', 'fresa', 'naranja', 'papaya')
vegetables = ('zanahoria', 'lechuga', 'tomate', 'pepino')
animal_products = ('jamón', 'mortadela', 'pescado', 'huevo')
food_stuff_tp = fruit + vegetables + animal_products
print(food_stuff_tp)

# 2. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print()
# 3. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[6:8])
print()

# 4. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[9:12])
print()

# 5. Delete the food_staff_tp tuple completely
food_stuff_tp = tuple(food_stuff_lt)
del food_stuff_tp
print()
# 6. Check if an item exists in tuple:
#7. Check if 'Estonia' is a nordic country

# 8. Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland','Norway', 'Sweden')