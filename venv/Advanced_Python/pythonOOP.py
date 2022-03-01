# class NameOfClass():
#
#     def__init__(self,param1,param2):
#
#         self.param1 = param1
#         self.param2 = param2
#
#     def some_method(self):
#         #perform some action
#         print(self.param1)
#

# num = 10
# num2 = 10.3
# num3 = '200'
# print(type(num))
# print(type(num2))
# print(type(num3))

# class Sample():
#     pass
#
# num = Sample()
#
# print(type(num))


class Sample():

    def __init__(self, name):
        self.name = name


x = Sample(name="Chase")


# print(x.name)


class Student():
    # These are Class Object Attributes
    species = "Humans"
    planet = "Earth"

    ##

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


student1 = Student(name="Chase", gpa=4.0)
student2 = Student(name="Rando", gpa=3.0)

print(student2.gpa)
print(student1.planet)


# Create another class

class Agent():
    origin = "USA"

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


x = Agent('Agent0', 6, 200)
x.weight = 210
print(x.weight)


# Exercise
# Create a class Dog which accepts the dog's name and breed
# Use this class to create 2 dogs: "German Shepherd: Hans" & "Labrador: Lou"
# Finally use an f-string to print the name of the 2 dogs
# ie 'Hans and Lou are friends'

class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

dog1 = Dog("German Shepherd", "Hans")
dog2 = Dog("Labrador", "Lou")

print(f"{dog1.name} and {dog2.name} are friends")