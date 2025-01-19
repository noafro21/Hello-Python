# Ejercicios practica para operadores aritméticos, de comparación y lógicos

# 1. Declare your age as integer variable
age = 34
print("My age is:", age)

# 2. Declare your height as a float variable
height = 1.75 
print("My heigth is:", height)
# 3. Declare a complex number variable
complex_number = 3 + 4j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_of_triangle = base * height / 2
print("The area of the triangle is: ", area_of_triangle)
print()
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter_of_triangle)
print()

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_of_rectangle = float(input("Ingrese la longitud del rectángulo: "))
width_of_rectangle = float(input("Ingrese el ancho del rectángulo: "))
area_of_rectangle = length_of_rectangle * width_of_rectangle
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
print("El area de rectángulo es: ", area_of_rectangle)
print("El perímetro de rectángulo es: ", perimeter_of_rectangle)
print()

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = float(input("Ingrese el radio del círculo: "))
area_of_circle = pi * radius ** 2
circumference = 2 * pi * radius
print("El area del círculo es: ", area_of_circle, "y su circunferencia es: ", circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2 
x = 0
y = 2 * x - 2
print("El valor de y es: ", y)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6, 10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("La pendiente entre los puntos (2, 2) y (6, 10) es: ", slope)

# 10. Compare the slopes in tasks 8 and 9.
print(y == slope)
print(y != slope)
print(y > slope)
print(y < slope)
print(y >= slope)
print(y <= slope)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = -6
y = x ** 2 + 6 * x + 9
print("El valor de y es: ", y)

# 12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.
length_python = len("python")
length_jargon = len("jargon")
print(length_python)
print(length_jargon)
print(length_python != length_jargon)
print()

# 13. Use and operator to check if 'on' is found in both 'python' and 'jargon'
print("on" in "python" and "on" in "jargon")
print()

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon'  in 'I hope this course is not full of jargon')
print()

# 15. There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')
print()

# 16. Find the length of the text python and convert the value to float and convert it to string
length_python = (len("Python"))
print(length_python)
print(float(length_python))
print(str(length_python)) 

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num_entero = int(input ("Ingrese un número entero: "))
module =num_entero % 2

if module == 0:
    print("El número", num_entero , "es par")
else:
  print("El número", num_entero , "no es par")  
  
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

num1, num2, floor_división = 7, 3, 2.7
print(num1 // num2 == int(floor_división))
print()

# 19. Check if type of '10' is equal to type of 10
print('10' == 10)
print()

# 20. Check if int('9.8') is equal to 10
print(int(9.8) == 10)
print()

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours_per_week = float(input("Ingrese las horas laboradas en la semana:\n "))
rate_per_hour= float(input("Ingrese la tarifa por hora:\n"))
pay_weekly = hours_per_week * rate_per_hour
print("El salario por la semana de la persona es: ", int(pay_weekly))

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.

day_of_years = 365
segundos_per_year = 86400
current_age = int(input("Ingrese su edad actual: "))
seconds_lived = current_age * day_of_years * segundos_per_year
print("Has vivido durante:", seconds_lived, "segundos")

# 23. Write a Python script that displays the following table

line1 = '1 1 1 1 1'
line2 = '2 1 2 4 8'
line3 = '3 1 3 9 27'
line4 = '4 1 4 16 64'
line5 = '5 1 5 25 125'

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
