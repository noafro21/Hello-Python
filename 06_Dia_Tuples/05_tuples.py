### Tuples ###
# Tuples are similar to lists, but they are immutable, meaning that the values inside a tuple cannot be changed.
# Also, tuples are written with parentheses, instead of square brackets.
# Tuples are faster than lists, and they are used when you do not want to change the values inside the tuple.

# Create a Tuple:
my_tuple = tuple()
my_other_tuple = ()

# Create a Tuple with values:
my_tuple = (34, 1.75, "Adonis", "Noa")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
