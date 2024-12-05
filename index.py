fruit = "orange"
num = 100

print(num)
num = num + 20 # this line is incrementing the num variable
print(num)

#this line is a list of items
fruits = "orange", 'mango', 'banana', 'cashew', 'guava'


print(fruit)

#more notes

fruit1 = "mango"
fruit2 = "orange"
num = 10

basket = ["mango", "orange", "guava, cashew", "banana", "guava", "mango"]

answer = 20

e = 2 #int
f = 9.18 #float
g = 8j #complex

#convert int to float
a = float(e)

#convert float to int
# b = int(c)

import random
print(random.randrange(1,10))


print(type(e))
print(type(f))
print(type(g))

k = 3.33e2
print(type(k))


thislist = ["apple", "banana", "cherry"]

print(thislist[2])

thislist[2] = "mango"

fruits = ("apple", "banana", "cherry", "mango", "gova", "cassava")

fruits = list(fruits)

fruits.append("corn")

print(fruits)

fruits = tuple(fruits)
print(fruits)

(first, second, third, fourth, fifth, sixth, seventh) = fruits
print(sixth)

fruits = ("apple", "banana", "cherry", "mango", "gova", "cassava")

for item in fruits:
    print(item)

    for item in fruits:
        more = item + " is a fruit"
        print(more)

print(len(fruits))

print(range(len(fruits)))
print(range(6))

#for item in fruits:
   # print(item)


    #print(fruits[0])

fruits = {"mango", "banana", "beans", "banana", "pear", "mango"}
#print(len(fruits))
#print(fruits)

fruits = {"mango", "banana", "beans", "banana", "pear", "mango"}
mylist = list(fruits)
print(mylist[1])

fruits = {"first": "mango", "second": "banana", "third": "beans", "fourth": "banana", "fifth": "pear", "sixth": "mango"}

fruitsAb = fruits.copy()

fruitsAb["abc"] = "Groundnut"

#print(fruits)


#print(fruits["first"])
#print(fruits)

myprops = fruits.keys()
myvalues = fruits.values()
entries = fruits.items()

#print(myprops)
#print(myvalues)
#print(entries)


    #print(fruit)




item1 = 20
item2 = 30

if item1 > item2:
    print("it is greater")
    print("we are matching forward")
    print("good job so far")
    if 2 < 5:
        print("wow we got inside the first if statement")
elif item1 < item2:
    print("it is greater")
    print("another printout")
elif item1 < item2:
    print("we have found the result")  
else:
    value = 50 + 20
    print("it is not true")    
    print(value)

