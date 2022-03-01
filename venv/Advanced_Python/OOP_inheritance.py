class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("hello")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")


# x = Person('John', "Smith")
#
# x.hello()
# x.report()

# Agent class inherits methods with Person class

class Agent(Person):

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    # Overriding report method here
    def report(self):
        print("I am here.")

    def reveal(self, passcode):
        if passcode == 123:
            print("I am a secret agent")
        else:
            self.report()


x = Agent('John', 'Smith', 'mr.X')
x.hello()
# x.report()
# x.reveal(12)
x.reveal(123)

print(x.code_name)
print("\n\n\n")


# Exercise
# Create a class Animal which accepts a name and species. IT should have a function called
# greet() which prints the statemnt: "Hi! My name is {name} and I am a {species}


class Animal():

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")


    # Then use this class to create the classes Cat and Dog. Each class should accept a name
    # and implement a method called sound() which prints the sound the animal typically makes


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    def sound(self):
        print("Wuff")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")

    def sound(self):
        print("Meow")

dog1 = Dog("Brutus")
dog1.sound()

cat1 = Cat("snickers")
cat1.sound()