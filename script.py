#!/bin/python3

#Variables And Methods
quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

print(len(quote))

name = "Simon" #string
age = 37 #int(30)
height = 5.10 #float float(5.9)

print (int(age))
print (int(30.9))

print ("My name is " + name + "I am " + str(age) + " years old")

age += 1
print (age)

birthday = 1
age += birthday
print(age)

print('\n')
#Functions
print ("Here is an example Function:")

def who_am_i(): #this is a function
    name = "Simon"
    age = 37
    print ("My Name is " + name + " I am " + str(age) + " years old.")

who_am_i()

#adding parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

#multiple parameters
def add(x,y):
    print (x + y)

add(7,7)

def square_root(x):
    print(x ** .5)

square_root(64)

print (square_root)

def nl():
    print('\n')

nl()

#Boolean expressions 
print ("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print (bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#Relational And Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 >5) and (5 > 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False
test_not2 = not False #True

nl()
#Conditional Statements

def drink(money):
    if money >= 2:
        return "You've got yourself a drink"
    else:
        return "NO drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "Nice try kid, come back when your 21"
    else: 
        return "Your too poor and too young kid"

print(alcohol(21,10))
print(alcohol(21,4))
print(alcohol(20,4))

nl()
#Lists - Have brackets []
movies = ["The Hangover", "Halloween", "The Rock", "The Exorcist", "Top Gun"]

print(movies[1]) #returns the second item
print(movies[0]) #returns the first item in the list
print(movies[1:4]) #returns all items from 2 to 4
print(movies[1:]) # returns all items in the list from second item
print(movies[:2]) # returns all item in the list up to the 3rd item
print(movies[-1]) # returns last item in the list 

print(len(movies))
movies.append("Jaws")
print(movies)

movies.pop(0)
print(movies)

nl()
#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
#Looping

#For Loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

#While loops - Execute as long as true

i = 1

while i < 10:
        print(i)
        i += 1

