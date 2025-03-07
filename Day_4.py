#built in functions and methods

print(len('hello'))

# string slicing
me = "helllo"
print(me[:3])

print(me.upper())

print(me.capitalize())

print(me.find('l'))

print(me.replace('o','m'))

#Booleans
#Boolean is true or false

name = 'Mumraiz'
is_cool = False

print(bool(0))
print(bool(1))

#Exercise Type Conversion

name = 'Mumraiz'
age = '26'
relationship_status = 'Single'

relationship_status = 'it\'s Complicatedddd' 

print(relationship_status)

birth_year = input('What year were you born?')

age = 2025 - int(birth_year)

print(f'You are {age} years old.')

# Exercise Password Checker

user = input('Enter the username:')

password = input('Enter the password:')

print(f'''Hey {user}. Your password  {'*' * len(password)}
      is {len(password)} characters long.''')

#list
#list is an ordered sequence of objects,
#lists are like arrays
#list is a data structure

li = [1,2,3,4,5]
li2 = ['a','b','c','d']
li3 = [1,2,7.9,'a',True]

shopping_cart = ['notebook','shirts','shoes']
print(shopping_cart[0])


# list slicing


