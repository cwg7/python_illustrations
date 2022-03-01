# Special methods
# 'dunder' methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} written by {self.author}"

    def __len__(self):
        return self.pages


myBook = Book('Python_Illustrations', 'Cwg7', 120)

print(myBook)
print(len(myBook))
print("\n\n")

# Exercise

# Create a class Students which accepts a list of names called names
# Implement functionality that returns the number of students your class object holds
# and another function which defines what happens if we want to print our instance
# When printing it, it should show the names of all the students


class Students():
    def __init__(self,names):
        self.names = names;

    def __str__(self):
        return f"{self.names}"

    def __len__(self):
        return len(self.names)

group1 = Students(['A','B','c'])
print(group1)
print(len(group1))