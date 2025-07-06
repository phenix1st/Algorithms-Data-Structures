# ------------------------------- FUNCTION LAMBDA --------------------------------
#   ANONYMOUS FUNCTION 
# [1] it has no name 
# [2] you can call it inline without defining it
# [3] you can use it in return data from another function 
# [4] you can use it as an argument in another function
# [4] Lamda function is used for simple functions and DEF handle the large tasks
# [5] Lambda expression is a one line single code not block of lines of code
# [6] Lambda type is a function 
# [7] Lambda function is used to create small anonymous functions
# --------------------------------------------------------------------------------

# Example of Lambda function
def say_hello(name) :
    return f"hello {name}"
print(say_hello("John")) # this will print hello John
# we can use lambda function to do the same thing
hello = lambda name : f"hello {name}"
print(hello("John")) # this will also print hello John
# --------------------------------------------------------------------------------
print(say_hello.__name__) # this will print say_hello
print(hello.__name__) # this will print "<Lmabda>" because it has no name
print(type(hello)) # this will print <class 'function'>