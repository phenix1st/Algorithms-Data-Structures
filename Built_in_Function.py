"""Python has a set of built-in functions.

Function	Description
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Returns the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the Unicode of the specified character
pow()	Returns the value of x to the power of y pow(base,exp,mod(%))
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators"""

#---------------------------- Built In Functions ----------------------------

round(50.556) #51
round(50.566, 2) # this meand the second digit result = 50.57

list(range(10)) #[1,2,3,4,5,6,7,8,9]
list(range(0,20,2)) #it starts from 0 to 20 and addng 2 every time [2,4,6,8,10,12,14,16,18,20]

print("hello" , "jack" , "9awd" , sep='/') # this will print the strings seperated by /
print("hello world " , end="looks it me at the end") #print that string in the end looks its me..
print("second line" , end="\n") #print new line at the end

print(pow(2,5,10)) # (2*2*2*2*2) %10
print(pow(2,5)) # 2*2*2*2*2

mynumber=(10,5,3,5,9,8,1,-1)
print(min(10,20,2,3,5,78,2))  # 2
print(min("X","Z","Oussama"))
print(min(mynumber))

a=['a','b','c','d','e','f']
print(a[:5]) #['a','b','c','d','e']
print(a[slice(5)]) # #['a','b','c','d','e']
print(a[slice(2,5)]) #it starts from 2 to 5  c d e

# ----------- MAP function ------------
# Map takes a fucntion + iterator
# Map called Map Because IT map the function on every element 
# the function can be Pre defined Funtion or lambda function 
# -------------------------------------








