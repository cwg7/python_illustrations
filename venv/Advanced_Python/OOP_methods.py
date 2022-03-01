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

myCircle = Circle(4)
#print(myCircle.radius)

print(myCircle.area())


print(myCircle.perimeter())
