# Python: High-level programming language

# =============================================================================
# Python is a high-level, interpreted, general-purpose programming language.
# Its design philosophy emphasizes code readability with the use of significant indentation.
# Python is dynamically-typed and garbage-collected.
# =============================================================================

# =============================================================================
# # Program - Set of intructions
# # Syntax - Set of rules
# # Compiler - Translates computer code written in one programming language into another language
# # Interpreter - Directly executes instructions one at a time
# # Variable - Value place holder
# # Constant - Unchange value which is asign to variable
# # Keywords - Some reserved words which language use itself
# # Case sensitive
# =============================================================================

# Write first Program - Hello World!
import datetime
print('Hello World!')

# Excercise 1

# Write a Name, Student ID and Email ID
print("Bob\n1234\nBob@gmail.com")

# Excercise 2

# Write a python code that add, subtract, multiply and divide the two numbers. Use 14 and 7

print(14 + 7)
print(14 - 7)
print(14 * 7)
print(14 / 7)

# Excercise 3

# Write python code that displays the numbers from 1 to 5 as steps

print('1\n    2\n        3\n            4\n                5')

# Excercise 4

# Write python code that outputs the following sentence (including the quotation marks and line break) to the screen:

# Sentence : "SDK" stand for "Software Development Kit", whereas "IDE" stands for "Integreted Development Environment".
print('"SDK" stands for "Software Development Kit", whereas\n"IDE" stands for "Integreted Development Environment".')

# Excercise 5

# Write a python code that prints the year you are born and then your age in 2020

# You are born in 1981. In the year 2020, you will be 39 years old.

yearBornIn = 1981
print("You are born in: ", yearBornIn)

ageIn2020 = 2020 - yearBornIn
print("In the year 2020, You will be", ageIn2020, "Years old!")

# Excercise 6

# Print sum of two variable
num1 = 10
num2 = 20

sum = num1 + num2
print('Sum:', sum)

# Excercise 7

# Write a code to ask user his name
name = input('Plese enter your name: ')
print('Hi,', name)


# Data Types:

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

x = "Hello World"	                            # str
x = 20	                                        # int
x = 20.5	                                    # float
x = 1j	                                        # complex
x = ["apple", "banana", "cherry"]	            # list
x = ("apple", "banana", "cherry")	            # tuple
x = range(6)	                                # range
x = {"name": "John", "age": 36}	                # dict
x = {"apple", "banana", "cherry"}	            # set
x = frozenset({"apple", "banana", "cherry"})    # frozenset
x = True	                                    # bool
x = b"Hello"	                                # bytes
x = bytearray(5)	                            # bytearray
x = memoryview(bytes(5))	                    # memoryview
x = None	                                    # NoneType


# Python Arithmetic Operators

# +	 Addition	x + y
# -	 Subtraction	x - y
# *	 Multiplication	x * y
# /	 Division	x / y
# %	 Modulus	x % y
# ** Exponentiation	x ** y
# // Floor division	x // y


# Check datatye
print(type(x))

# User Interactive programming
name = input("Please enter your name: ")  # default output is str
print('Hello,', name)

age = int(input("Please enter your age: "))
age = age+1
print("Happy birthday, You are now", age, "years old!")

# Conditions and If statements: if-elif-else

a = 200
b = 33

if b > a:

    print("b is greater than a")

elif a == b:
    print("a and b are equal")

else:
    print("a is greater than b")

# For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String

for x in "banana":
    print(x)


# The pass Statement

for x in [0, 10, 2]:
    pass


# The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# The range() Function

for x in range(6):
    print(x)

# The range() Function - Using the start parameter:

for x in range(2, 6):
    print(x)

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
    print(x)

# Else in For Loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Tuple
# Tuple items are ordered, unchangeable, and allow duplicate values

thistuple = ("apple", "banana", "cherry")
print(thistuple)


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Sets

# Sets are used to store multiple items in a single variable
# Set items are unordered, unchangeable, and do not allow duplicate values.

myset = {"apple", "banana", "cherry"}
print(myset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Dictionaries
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionary Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Dictionary Length

print(len(thisdict))

# Python While Loops

i = 1
while i < 6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

    i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

    i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


def my_function():
    print("Hello from a function")


my_function()


# Lambda

# Syntax: lambda arguments : expression

def x(a): return a + 10


print(x(5))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))

# Arrays

# Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]

cars[0] = "Toyota"
cars

# Looping Array Elements
for x in cars:
    print(x)

# Length of an Array
x = len(cars)

# Adding Array Elements
cars.append("Honda")


# Datetime

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

# Return the year and name of weekday

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects


x = datetime.datetime(2020, 5, 17)
print(x)


# String Formatting

# To make sure a string will display as expected, we can format the result with the format() method.

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

