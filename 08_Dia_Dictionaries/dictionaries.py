### Dictionarios ###

my_dict = dict()
my_other_dict = {}   
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'name':'Adonis', 'first_name':'Frometa', 'age': 34, 1: 'Python'}

my_dict = {'name':'Adonis', 
           'first_name':'Frometa', 
           'age': 34,
           'lenguajes': { 'Python', 'Java', 'CCs', 'JavaScript'},
           1:1.75
           
           }
print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict['name'])
my_dict['name'] = 'Adonis Frometa'
print(my_dict['name'])  
print(my_dict[1])

my_dict['city'] = 'Guantánamo'
print(my_dict)

print ("Adonis" in my_dict)
print ('first_name' in my_dict)

print(my_dict.get('name'))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(( 'name', 'first_name'))) # Crea un diccionario con las claves que le pasamos y les asigna el valor None a cada una de ellas 



