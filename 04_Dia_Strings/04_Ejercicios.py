# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print()
string1 = 'Thirty '
string2 = 'Days '
string3 = 'Of '
string4 = 'Python '
print(string1 + string2 + string3 + string4)
print()

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word1 = 'Coding'
word2 = 'For'
word3 = 'All.'
space = ' '
complete_sentence = word1 + space + word2 + space + word3
print(complete_sentence)
print()

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4. Imprima la variable empresa utilizando print() .
print(company)
print()

# 5. Print the length of the company string using len() method and print().
print(len(company))
print()

# 6. Change all the characters to uppercase letters using upper() method.

print(company.upper())
print()

# 7. Change all the characters to lowercase letters using lower() method.

print(company.lower())
print()

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())
print()

# 9. Cut(slice) out the first word of Coding For All string.
#print(company[6:14])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.find('d'))
print(company.index('g'))
print(company.find(company))


# 11. Replace the word coding in the string 'Coding For All' to Python.
company = company.replace('Coding', 'Python')
print(company)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
company = company.replace("For All"," En Treita Días")
print(company)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
print(company.split())

company = "Coding, For, All"
print(company.split(" , "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(company.split(" ,"))

# 15. What is the character at index 0 in the string Coding For All.
company = "Coding For All"
print(company[0])

# 16. What is the last index of the string Coding For All.
company = "Coding For All"
print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.

print(company[10])

# 34. Use a tab escape sequence to write the following lines.

print("Name \tAge\tCountry \tCity")
print("Adonis \t34\tCuba           \tGuantánamo")
print()

# 35. Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))
print()
print("The area of a circle with radius %d is %d meters square."%(radius, area))
print()


# 36. Make the following using string formatting methods:

print('{} + {} = {}'.format(8, 6, 8 + 6))
print('{} - {} = {}'.format(8, 6, 8 - 6))
print('{} * {} = {}'.format(8, 6, 8 * 6))
print('{} / {} = {:.2f}'.format(8, 6, 8 / 6))
print('{} ** {} = {}'.format(8, 6, 8 ** 6))
print('{} % {} = {}'.format(8, 6, 8 % 6))
print('{} // {} = {}'.format(8, 6, 8 // 6))

# Realizo una la tabla de multiplicar solicitando la  que desea solicitar 

a = int(input("Ingrese la tabla que desea aprender: "))
print("A continuacion se muestra la tabla del: ", a  )
print('{} * {} = {}'.format(a, 1, a * 1))
print('{} * {} = {}'.format(a, 2, a * 2))
print('{} * {} = {}'.format(a, 3, a * 3))
print('{} * {} = {}'.format(a, 4, a * 4))
print('{} * {} = {}'.format(a, 5, a * 5))
print('{} * {} = {}'.format(a, 6, a * 6))
print('{} * {} = {}'.format(a, 7, a * 7))
print('{} * {} = {}'.format(a, 8, a * 8))
print('{} * {} = {}'.format(a, 9, a * 9))
print('{} * {} = {}'.format(a,10, a * 10))



