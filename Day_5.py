#matrix

matrix = [
    [1,2,3],
    [3,5,7],
    [3,6,5]
    ]

matrix1 = [
    [1,4,1],
    [0,1,0],
    [1,0,1]
    ]

print(matrix1[0][1])

#List Methods

base = [1,45,5,6,6,7]

print(len(base))

#adding
new = base.append(500)
new = base
print(new)

ins = new.insert(5,6666)
ins = base
print(ins)

ext = ins.extend([980])
ext = ins
print(ext)

#removing

ext.pop(0)
print(ext)

ext.remove(45)
print(ext)

clr = ext.clear()

print(clr)

balls = ['a','b','c','d','x','t']

print(balls.index('b',0,2))

print(1 in balls)

print(balls.count('a'))

#print(balls.sort())

#balls.sort()

print(balls)

print(sorted(balls))
balls.sort()
balls.reverse()

print(balls)


print(balls[::-1])

print(list(range(100)))

sentence = '!'

new_sen = sentence.join(['hi','my','name','is','xyz'])

print(new_sen)


#List Unpacking

b,a,c,*oth = [1,2,3,9,8,7,6,5]

print(b)

print(oth)

# Dictionary
# unordered key value pair
dictionar = {
    'a' : [1,3,5],
    'b' : 'hi'
}

print(dictionar['b'])

print(dictionar)

# dictionary hold more values than list
# a key has to be unique
dict = {
    123 : [1,3,4,]
    
        }

print(dict[123])

# Dictionary Methods

dict1 = {
    'a' : [1,3,4,],
    'b' : 'hii'
        }

# getting default value if h not exist in dictionary
print(dict.get('h',8))


print('a' in dict1.keys())

print(dict1.items())

print(dict1.copy())

print(dict1.pop('a'))

print(dict1.update({'b': 5}))

print(dict1)


# Tuple
# Tuple is immutable --- not changeable
# ususally faster than list
my_tuple = (1,2,3,4,5)

new_tuple = my_tuple[1:2]

print(new_tuple)



# tuple has 2 methods

print(my_tuple.count(2))

print(my_tuple.index(4))

# Sets

# Unordered collection of unique objects
# not support index
my_set = {1,2,3,4,44,4,4}

print(my_set)

my_set.add(100)
print(my_set)

my_list = [1,2,3,4,5,6,6]

print(set(my_list))

# sets methods
your_set = {4,88,9}
print(my_set.difference(your_set))
print(my_set.discard(1))

print(my_set)

print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

print(my_set | your_set)

print(my_set & your_set)

print(my_set.issubset(your_set))

print(your_set.issuperset(my_set))