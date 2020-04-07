#!/bin/python3

import sys #system function and parameters
from datetime import datetime as dt #import with alias
print(dt.now())

my_name = "Simon"
print(my_name[0])
print(my_name[1]) #prints out the second character of my_name

sentence = "This is a sentence."
print (sentence[:4])

print(sentence.split()) #prints out the sentence with splits occuring on the space as its the natural delimiter

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He Said, \"Give me all your money\"" #using the \ I am escaping the characters and treating anything within the \  \ as a string.
print(quote)

too_much_space = "                                            Hey                         "
print(too_much_space.strip())
print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Rock"
print("My favourite movie is {}.".format(movie))

#Dictionaries - key/value pairs {}
drink = {"Long Island Iced Tea": 10, "Cosmo": 7, "White Russian": 8} #drink is key, price is value 
print(drink)

employees = {"Finance":["Bob", "Linda", "Tina"], "IT": ["Simon", "Sam", "Jon"], "HR": ["Lou", "Jaimie"]}
print(employees)

employees['Legal'] = ["Mr. Bond"] #add new key:value pair
print(employees)

employees.update({"Sales": ["Andy", "Ollie"]}) #add new key:value pair
print(employees)

drink['White Russian'] = 8
print(drink)

print(drink.get("White Russian"))

