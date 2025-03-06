#strings
print(type("hi"))

username = 'super'
password = 'machine'

long_str = ''' How are you 

9asdg 

'''
print(long_str)

first_name = 'Mumraiz Babar'
last_name = 'Khan'

full_name = first_name +' '+ last_name

print(full_name)

#string concatenation
#only works with string
# Type Conversion
print(type(str(100)))

#Escape Sequence

weather =  "it\'s \"kind of\" sunny \n hope you are well"
print(weather)

#formatted strings

name = 'john'
age = 27

print(f'hi {name}. You are {age} years old')

#print('hi{}.you are {} years old'.format(name,age))


self = '01234567'

#[start:stop:stepover]

print(self[0:5:2])
print(self[::-2])

#immutability
# string are immutable, we cannot change strings.

