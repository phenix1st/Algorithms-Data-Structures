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
