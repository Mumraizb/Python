# List Slicing
# lists are mutable, change able
shopping_cart = ['notebook',
                 'shirts','shoes','glasses']

print(shopping_cart[0:3])

shopping_cart[0] = 'phone'
print(shopping_cart)

# slicing means to create the copy of that list

shopping_cart[0] = 'nothing'

new = shopping_cart[:]
new[0] = 'how'
print(new)
print(shopping_cart) 

list = [1,2,3,4]

copy = list[:]
copy[1] = 'ert'
print(list)
print(copy)
