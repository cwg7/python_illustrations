# OOP methods

class Circle():

    pi = 3.14
# setting default radius value here
    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius**2 * Circle.pi

    def perimeter(self):
        return 2*self.radius *Circle.pi

    def multiply_radius(self,number):
        self.radius = self.radius*number
        print(f"Radius has been changed to {self.radius}")

myCircle = Circle(4)
#print(myCircle.radius)

print(myCircle.area())

print(myCircle.perimeter())

print(myCircle.multiply_radius(3))


# Exercise

#Create a class Dog that takes the dog's name, breed, and age.
# Define a method called calculate_human_age that multiplies the dog's age
# by 7 and returns the result to an estimate of its age in human years
# Make sure that the method does not accept any arguments besides self

class Dog():
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def calculate_human_age(self):
        return self.age * 7

dog1 = Dog('Buzz', 'Boston', 5)

print(dog1.calculate_human_age())