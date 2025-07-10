mytuple = ("apple", "banana", "cherry")
#All these objects have a iter() method which is used to get an iterator:
myit = iter(mytuple) 

print(next(myit))
print(next(myit))
print(next(myit))
#Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"
#Iterate the characters of a string:
for x in mystr:
  print(x)

#Example
  class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))