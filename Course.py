from convertrs import kg_to_lbs, lbs_to_kg
from ecommerce.shipping import calc_shipping
import ecommerce.shipping
from convertrs import *
import convertrs
import random
import math  # this is a library with math functions
print("hello world")
print("***" * 10)  # prints the string 10 times
print(" adem hamdi" * 2)  # prints the string two times
x = 1
student = 100
donc = "jack"
flot = 1.555
m = -1.5
jakc = True
bro = False
text = """ 
hi jhon this bro go jump off the building
"""
print(len(donc))  # len fucntion return the length of string
print(donc[0])  # printf the first element of string like c language
print(donc[-1])  # this return the last character of the string
print(donc[0:3])  # prints the first three characters of the string
print(donc[:3])  # prints the same as the command beofre
print(donc[:])  # returns the original string
# we use "\'" or '\"' to printf the quotities in the string becaus if we dont python wont read the last of our string and stop in middle
str = "programmign \"python"
# this called escape sequences
# we can use \n to printf the new line
# prints hello in the first line and world in the second lin
print("hello \n world")
# \\ is to include a back slash '\' in your string
# concatenation using +
ah = "ahmed"
bo = "bodi"
ya = ah+bo
print(ya)
print(ah+" "+bo)  # this is the same as the command before but with space
ja = f"{ah} {bo}"
print(ja)  # this is the same as the command before with space also
jak = f"{len(ah)} {bo}"
print(jak)  # so we can put any type of variables
# string methods
test = "ahmed"
test.upper()  # it gives u the upper case of the string
test.lower()  # it gives u the lower case of the string
test.title()  # it capitalize the first character of each string
loren = "   programming"
# this is to remove the spaces from the string
loren.strip()  # this is to remove the spaces from the string
loren.lstrip()  # this is to remove the spaces from the left of the string
loren.rstrip()  # this is to remove the spaces from the right of the string
# this is to find the index of the first occurrence of the string
test.find("ahm")
# this will return -1 because this capital letters they exist but in lower case
test.find("AHM")
# this is to replace the first occurrence of the string with the second string
test.replace("h", "k")
print("pro" in test)  # this is to check if the string exist in the string or not
# this is to check if the string dont exist in the string or not
print("kaka" not in test)
# Numbers
# int #float # complex
x = 1
y = 2.234
z = 1+3j  # z=a+bj
print(10 + 5)  # this is to add two numbers
print(10 - 5)  # this is to subtract two numbers
print(10 * 5)  # this is to multiply two numbers
print(10 / 3)  # this is to divide two numbers
print(10 // 3)  # this is to return the qotient of the division of two numbers
print(10 % 3)  # this is to return the remainder of the division of two numbers
print(10 ** 5)  # this is to return the power of the number
x = x+3
x += 3  # this is the same as the command before
round(y)  # this is to return the number with the specified number of digits after the decimal point
abs(-2.9)  # this is to return the absolute value of the number

# result is 3 this is to return the smallest integer not less than the given number
math.ceil(3.3)
math.fabs()  # this is to return the absolute value of the number
math.factorial()  # this is to return the factorial of the number
math.cos()  # this is to return the cosine of the number
math.sin()  # this is to return the sine of the number

# type conversion
# this is to get the input from the user and input function return always string
k = input("x:")
# y=k+1 this is an error we cant concatenate str with int(not same type)
type(x)  # this is to return the type of the variable
int(k)  # this is to convert the string to integer
float(k)  # this is to convert the string to float
bool(k)  # this is to convert the string to boolean
str(k)  # this is to convert to a string
# example
p = input("p :")
s = int(p)+1
print(f"p : {p} and s : {s}")  # this is to print the string with values
# in boolean we have the falsy values and truthy values
# falsy values : 0 , None , False , empty string , empty list , empty dictionary, ""
# truthy values : 1 , True , any string , any list , any dictionary , anything else

# Comparision operators
# < > == != <= >=
# it is permissible to compare string with operators directly like normal algo
# it is permissible to compare numbers with operators directly like normal algo
# "bag" > "apple" this gives u true because Compare first letters:'b' vs 'a' Unicode of 'b' = 98, 'a' = 97
# Since Python finds that 'b' > 'a', it doesn't need to compare the rest of the characters. It already knows "bag" > "apple" is true.
# ord function gives u the unicode of the word or letter
# ord('a') #this is to return the unicode of the letter

# conditional statements
temp = 35
if temp > 30:
    print("the temperature is high")
else:
    print("take a shower")

if temp < 20:
    print("take a jacket")
elif temp > 45:
    print("take a warm water")
else:
    print("take a normal water")
    # in python we can use the else if statement like in other languages but we can use the elif

hotrud = 35
if hotrud > 30:
    message = "hello"
else:
    message = "fuckoff"
# cleaner way to write th ecode above it is called TERNARY OPERATOR
message = "hello" if hotrud > 30 else "fuckoff"
print(message)  # this is to print the message

# Logical operators
# AND operator
# OR operator
# NOT operator
# the same in algo
t = True
f = False
if t and f == True:  # if (t and f) or not t: this just exemple of statement
    print("hello")
else:
    print("fuckoff")
    # the same in algo

# chain comparision operators
age = 11
if age >= 18 and age < 30:
    print("you are adult")
if 18 <= age < 30:
    print("you are adult")

# Loops
# for loop
for number in range(3):
    print("hello world", number)
# this printd hello world three times
# and number is int variable that is used to print the number of the loop ( index of the loop)
for number in range(3):
    print("hello world", number + 1, (number + 1)*"*")
    # this printd hello world three times with the number of the loop printed with *
for number in range(1, 4):
    print("hello world", number)
    print("hello world", number, number * "*")
# here we can see that the range is from 1 to 3 (4 is excluded)

# For..else
successful = True
for number in range(3):
    print("hello world", number)
    if successful:
        break
print("loop finished")  # this is printed because the loop is finished
# the else statement is executed when the loop finishes normally (i.e., not by the break statement
# For..else is used to execute a block of code when the loop finishes normally (i.
successf = False
for number in range(3):
    print("hello world", number)
    if successf:
        break
else:
    print("attempted 3 times and failed")
# this will hello world three times then print attempted 3 times and failed

# Nested Loops
for x in range(5):
    for y in range(5):
        print(f" x = {x} , y = {y}")

# iterables
print(type(5))  # int
print(type(range(5)))  # this will return a range object
# special types
# iterable
for x in "python":
    print(x)  # this will print each character of the string
# like in c language this a way to travel in a string to print each character
for x in [1, 2, 3, 4, 5]:
    print(x)  # this will print each number of the list
# for item in shopping_cart :
#   print(item) #this shopping cart is an object that is iterable and im the one who define it as i want

# While Loops
number = 100
while number > 10:
    print(number)
    number //= 2  # this will print each number from 100 to 80
# example
command = ""
while command != "quit":
    command = input("enter a command: ")
    # this will keep asking the user for a command until the user types quit
    print("Echo", command)
    # if we type quit in upper case the program wont stop working cause there is different between upper case and lower case words
# solution
while command.lower() != "quit":
    command = input("enter a command: ")
    # this will keep asking the user for a command until the user
    print("Echo", command)
# infinite Loop
while True:
    command = input("enter a command: ")
    # this will keep asking the user for a command until the user
    print("Echo", command)
    if command.lower() == "quit":
        break  # this will stop the loop when the user types quit

# Function / Arguments


def greet():
    print("Hello, World!")
    print("welcome to DZ")


greet()  # this will print hello world and welcome to dz


def greet(first, last):
    print("Hello, World!")
    print(f"welcome to DZ {first} {last}")


greet("Hamdi", "Adem")  # this will print hello world and welcome to dz hamdi adem

# types of Funtions
# 1-Perform a Task
# 2-return a value
# writing the greet exmple in the second type


def greet2(name):
    return f"Hello, {name}!"


ret_msg = greet2("adem")
print(ret_msg)  # this will print hello adem
# this will open a file called context.txt and write in it
file = open("context.txt", "w")
file.write(message)  # this will write the message in the context.txt file

# this will print hello world and welcome to dz jack ma and printf None because this the return value of the greet fucntion
print(greet("jack", "ma"))

# keyword arguments
# keyword arguments are arguments that are passed to a function with the name of the parameter
# they are useful when you don't know how many arguments a function will take
# they are also useful when you want to pass arguments by name instead of by position
# the greet function with keyword arguments


def greet(first, last, age, country):
    print(f"Hello, {first} {last}!")
    print(f"you are {age} years old")
    print(f"you are from {country}")


greet(first="jack", last="ma", age=20, country="egypt")

# *args


def multiply(x, y):
    return x*y

# we want this multiply(2,3,4,5) but we cant so we need to use *


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

    print(numbers)  # this will print (2,3,4,5)
    # this a topples (object)
    # this topples are iterable too


# Different Funtions

print(random.random())           # 0.234... (random float 0 to 1)
print(random.randint(1, 10))     # 7 (random int between 1 and 10)
print(random.uniform(1.5, 5.5))  # 3.17 (random float between 1.5 and 5.5)

my_list = ['sword', 'shield', 'bow']
print(random.choice(my_list))    # 'shield'

random.shuffle(my_list)
# ['bow', 'shield', 'sword'] — order changes randomly
print(my_list)
# example
# Simulating dice rolls
dice = random.randint(1, 6)
print(f"You rolled a {dice}")

# Lists
# Lists are ordered collections of items that can be of any data type, including strings, integers
# Lists are denoted by square brackets [] and are mutable, meaning they can be changed after creation
# Lists are ordered, meaning that items have a specific position in the list
# Lists are indexed, meaning that each item has a specific index or position in the list
# Lists are mutable, meaning that they can be changed after creation
# example
names = ["adem", "yaakoub", "mohammed", "jalil", "seddiki", "wassim"]
print(names[0])  # this will print adem
print(names[-1])  # this will print wassim
print(names[2:])  # this will print mohammed,jalil,seddiki,wassim
print(names[:])  # this will print all the list

# 2D Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# to access the items we use matrix[][] rows first than colomns
print(matrix[0][2])
matrix[0][2] = 225
print(matrix)  # this will print [[1,2,3],[4,5,6],[7,8,9]

# this means each time rows will have a list of the three first [1,2,3] then [4,5,6] then [7,8,9]
for rows in matrix:
    for item in rows:  # this means each time item will have a number 1,2,3 then 4,5,6 then 7,8,9
        print(item)  # this will print each number

# to insert a new element from the end we use .append
# to insert a new element from the middle or beginning or the end we use .insert
# hamdi will be in index 2 new list is "adem","yaakoub","hamdi","mohammed","jalil","seddiki","wassim"
names.insert(2, "hamdi")
# to remove a item we use .remove
names.remove("hamdi")  # hamdi will be removed
# to remove all the list elements we use clear
names.clear()  # this empties the list []
num = [1, 2, 3, 3, 4, 6, 5]
# to remove the elements from the end we use .pop  removes from the end in default (fargha)
num.pop()
# to find the index of an element we use .index
num.index(2)  # this will return 1 which is the index of number 2 in the list or the first occurence of an element in other meanings
# if we pass a value that dont exist in the list we get error in terminal
# a solution
print(50 in num)  # this will return False because 50 doesnt exist in num list
# to search for the occurences of an element we use .count
print(num.count(3))  # this will return 2 occurences of 3
# to sort any list we use .sort
num.sort()  # this way the list is sorted
# to reverse any list we use .reverse
num.reverse()  # this way our list is reversed
num31 = num.copy()  # to copy a list into another list we use .copy this way num31 == num

# Tuples
# this one is a tuple when we change [] with () it means this is a tuple
fork = (1, 2, 3)
# tuples are imutaple this means are unchangeable we cant add or remove with them
# there is no pop or remove or append in tuples
fork.count("hamdi")
fork.count(2)  # this return the number of occcurences in the tuple
# this will return 1 which is the index of number 2 in the list or the first occurence of an element in tuple
fork.index(2)
# Access tuples
print(fork[0])  # this will print 1

# Unpacking
coordinates = (1, 2, 3)
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
# this is too much writing in code so we have a powerful feature called unpacking
a, b, c = coordinates  # this is the same to first writting
# this will give the first element to a and second to b and third to c
# this feature is not just for tuples we can use it too with lists

# Dictionairies
customer = {
    "name": "hamdi",
    "age": 25,
    "city": "tunis"
}  # the keys should be uniq we cant have two keys with the same name
customer["name"] = "jack"  # this will change the value of the key "name"
# to add a new key we use .add
# this will add a new key with the value "tunisia"
customer["country"] = "tunisia"
print(customer["name"])  # this will print hamdi
# to add a new key we use .update
# this will add a new key called country with value tunis
customer.update({"country": "tunis"})
# to remove a key we use .pop
customer.pop("city")  # this will remove the key called city
# to check if a key exists we use .get
# this will print hamdi and the key should be written the same way as it is in the dictionary in same form (lower or upper)
print(customer.get("name"))
# this will return None because birthday is not a key in the dictionary
print(customer.get("birthday"))
# this will print not found because birthday is not a key in the dictionary
print(customer.get("birthday", "not found"))
# to check if a key exists we use .get with default value
print(customer.get("country", "tunis"))  # this will print tunis
print(customer.get("name", "not found"))  # this will print hamdi

# try except to handle exceptions
try:
    years = int(input("Enter your age : "))
    print(years)
except ValueError:
    # this will print invalid input if the user enter a string instead of
    print("Invalid input")

# try except with multiple except
try:
    years = int(input("Enter your age : "))
    income = 20000
    risk = income / years
    print(years)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    # this will print you didn't enter your ag
    print("You didn't enter your age your cant be zero")

# Classes


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

        def drive(self, miles):
            self.mileage += miles
            print(f"You drove {miles} miles")

            def describe_car(self):
                print(
                    f"This car is a {self.year} {self.brand} {self.model} with ")

# class EmailClient : #this is a class with two names to name a class with two words we use pascal case so we capitalize the first char of each word we dont use "_"


class Point:
    def Move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.Move()
point1.draw()
print(point1.x)  # this will print 10
print(point1.y)  # this will print 20
point1.draw()  # this will print draw

# to call a method we use the dot operator and the name of the method
# to access an attribute we use the dot operator and the name of the attribute
# to create an object we use the class name and the parentheses

# Constructors


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point6 = Point2(20, 1)
# example


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"hello world {self.name}")


jhon = person("hamdi adem")
jhon .talk()  # this will print hello world

# inheritance
# we use inheritance so we dont rewrite or duplicate or write again the same code in different classes
# we can inherit from one class to another class
# there is a lot of types of inheritance in python
# the easiest one is single inheritance


class Mamall():
    def walk():
        print("walk")


class Animal(Mamall):
    def eat(self):
        print("eat")
    # we can either use pass if we dont want to add anything else or we create another special method for this class
    pass  # here we used pass


dog = Animal()
dog.walk()  # this will print walk which he iherited it from Mamall class
dog.eat()  # this will print eat

# Modules
# Module in python is basically a file with some python code we use it to organize our code and make it reusable
# now we are gonna call a file convertors.py that uses fucntions to convert between different units of measurement
# we are gonna call it in our main.py file
# we can import all the functions from the module using the from keyword
print(convertrs.kg_to_lbs(50))  # this will print 110
print(convertrs.lbs_to_kg(110))  # this will print 50
# 2nd method is better
print(kg_to_lbs(50))  # this will print 110
print(lbs_to_kg(110))  # this will print 50
# 3rd method is the best
print(kg_to_lbs(50))  # this will print 110
print(lbs_to_kg(110))  # this will print 50

# Packages
# Package is a container of a lot of modules
# we use it to organize our code and make it reusable
# we can create a package by creating a folder and inside the folder we create a file called __
ecommerce.shipping.calc_shipping()  # this will print 10.0
# 2nd method
calc_shipping()  # this will print 10.0

#Working With Files and Directories
# we can use the os module to work with files and directories
import os
# we can use the os.getcwd() function to get the current working directory
print(os.getcwd())  # this will print the current working directory
# we can use the os.mkdir() function to create a new directory
# we can use the os.rmdir() function to remove a directory
# we can use the os.rename() function to rename a directory
# we can use the os.remove() function to remove a file
# we can use the os.listdir() function to get a list of all files and directories in th
# we can use the os.path.join() function to join two or more path components together
# we can use the os.path.exists() function to check if a file or directory exists
# we can use the os.path.isfile() function to check if a path is a file
# we can use the os.path.isdir() function to check if a path is a directory
# we can use the os.path.getsize() function to get the size of a file
# we can use the os.path.getmtime() function to get the last modified time of a fil
# we can use the os.path.getctime() function to get the creation time of a file
# we can use the os.path.getatime() function to get the last accessed time of a file
# we can use the os.path.getatime() function to get the last accessed time of a file

from pathlib import Path
# we can use the Path class to work with files and directories
# we can use the Path.mkdir() method to create a new directory
# we can use the Path.rmdir() method to remove a directory
# we can use the Path.rename() method to rename a directory
# we can use the Path.remove() method to remove a file
# we can use the Path.exists() method to check if a file or directory exists
# we can use the Path.is_file() method to check if a path is a file
# we can use the Path.is_dir() method to check if a path is a directory
# we can use the Path.stat() method to get information about a file or directory
Path.glob() #Path.glob() is a method from Python’s pathlib module used to search for files and directories matching a specified pattern (using Unix shell-style wildcards like *, **, ?).
print(Path.glob('*.txt')) # prints all .txt files in the current directory
print(Path.glob('*.py')) # prints all .py files in the current directory
print(Path.glob('*.xcl')) # prints all .xcl files in the current directory
# this way nothing will be printed because it is an error 
#so iterate over it and we use a loop
for file in Path.glob('*.txt'):
    print(file) # prints all .txt files in the current directory
    # we can use the Path.iterdir() method to iterate over the files and directories in a path
    # we can use the Path.read_text() method to read the contents of a file
    # we can use the Path.write_text() method to write to a file
    # we can use the Path.read_bytes() method to read the contents of a file in binary mod
    # we can use the Path.write_bytes() method to write to a file in binary mode
for file in Path.glob('*'):
    print(file) # prints all files and directories in the current directory

#Pypi and Pip
# we can use pip to install packages from the Python Package Index (PyPI)
# we can use pip to install packages from a local directory
# we can use pip to install packages from a URL
# we can use pip to uninstall packages
# we can use pip to freeze packages
# we can use pip to list packages
# we can use pip to search packages
# we can use pip to show package information
# we can use pip to upgrade packages
# we can use pip to downgrade packages
# we can use pip to show package dependencies
# we can use pip to show package version
# we can use pip to show package version history
# we can use pip to show package changelog
# we can use pip to show package documentation
# we can use pip to show package license
# we can use pip to show package author
# we can use pip to show package maintainer
# we can use pip to show package homepage
# we can use pip to show package description
# we can use pip to show package keywords
# we can use pip to show package classifiers
# we can use pip to show package download count
# we can use pip to show package rating
# we can use pip to show package reviews
# we can use pip to show package ratings
# we can use pip to show package ratings history
# we can use pip to show package ratings distribution
# we can use pip to show package ratings distribution history

#Web Scraping
# we can use the requests library to send HTTP requests
# we can use the BeautifulSoup library to parse HTML and XML documents
# we can use the Scrapy library to build web scrapers
# we can use the Selenium library to automate web browsers
# we can use the PyQuery library to parse HTML and XML documents
# we can use the lxml library to parse HTML and XML documents
# we can use the xml.etree.ElementTree library to parse XML documents
# we can use the xml.dom.minidom library to parse XML documents
# we can use the xml.sax library to parse XML documents
# we can use the xml.parsers.expat library to parse XML documents
# we can use the xml.parsers.xmlparser library to parse XML documents

