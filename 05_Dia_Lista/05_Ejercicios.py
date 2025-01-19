#Ejercicios: Nivel 1
# 1. Declare an empty list
lst = list ()
list = []
print()
# 2. Declare a list with more than 5 items
ice_cream_flavors = ['fresa', 'chocolate', 'vainilla', 'café' , 'naranja', 'coco', 'guanábana']

# 3. Find the length of your list
list_length = ice_cream_flavors
print(len(list_length))
print()
# 4. Get the first item, the middle item and the last item of the list
print(ice_cream_flavors[0])
print(ice_cream_flavors[3])
print(ice_cream_flavors[6])
print()

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types =['Adonis', 34, 1.75, 'casado','San José, Costa Rica']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(mixed_data_types)
print(it_companies)
print()

# 8. Print the number of companies in the list
print(len(it_companies))
print()

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
print()

# 10. Print the list after modifying one of the companies
modifying_it_companies = it_companies
modifying_it_companies[1] = 'Firefox'
print(modifying_it_companies)
print()

# 11. Add an IT company to it_companies
it_companies.append('Samsung')
print(it_companies)
print()

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4,'Motorola')
print(it_companies)
print()

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies [0] = 'FACEBOOK'
print(it_companies)
print()
# 14. Join the it_companies with a string '#;  '

# 15. Check if a certain company exists in the it_companies list.

print('Google' in it_companies)
print('Apple' in it_companies)
print()
# 16. Sort the list using sort() method
#it_companies.sort()
print(it_companies)
print()
# 17. Reverse the list in descending order using reverse() method
#it_companies.reverse()
print(it_companies)
print()
# 18. Slice out the first 3 companies from the list

print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[4:7])
print()
# 20. Slice out the middle IT company or companies from the list
print(it_companies[2:5])

# 21. Remove the first IT company from the list
#it_companies.remove('IT')
print(it_companies)

# 22. Remove the middle IT company or companies from the list
#it_companies.pop(4)
print(it_companies)

# 23. Remove the last IT company from the list
#it_companies.pop(7)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
print()

# 25. Destroy the IT companies list
#del it_companies
print(it_companies)
print()

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)
print()

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, { 'Python', 'SQL' })
print(full_stack)
print() 

#Exercises: Level 2

# 28. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print()

# Add the min age and the max age again to the list 
ages.append(ages[0])
ages.insert(0, 19)
print(ages)
print()

# Find the median age (one middle item or two middle items divided by two)
print(ages[5])
print()

# Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(average)