number=int(input("enter the number for fibonacci sequence f(n) : "))
def fibonacci(n):
    if n <= 1:
        return n 
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(number))