#Operator precedence

#print(20 - 3*4)

#1. Brackets()
#2. ** power
#3. * /
#4.//
#5. + -

#print((20-3) + 2 **3)

print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) #45

print((5 + 4) * (10 / 2)) #45

print(5 + (4 * 10) / 2) #25

print(5 + 4 * 10 // 2) #25

print(45 // 2) 

#binary

print(bin(5))

#variables

name = 'Mumriaz'
age = 26

print("My name is",name,"and age is",age)

#constants 
PI = 3.14

print(PI)

a,b,c = 1,4,5
print(a,b,c)

#augmented assinment operator

some_value = 5 + 2

some_value = some_value + 3
some_value += 1

print(some_value)


