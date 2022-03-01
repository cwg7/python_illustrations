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

    def __init__(self,name):
        self.name = name


x = Sample(name = "Chase")
print(x.name)

