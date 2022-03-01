#errors and exception handling

# cannot 'catch' syntax error
#print("hello)

# example of catching a type error

# try:
#     print('10' + 10)
#
# except IOError:
#     print("You have an input/output error")
#     print("Did you check the file permissions?")
# except TypeError:
#     print("You are using the wrong data types")
#
# except:
#     print("Hey you got an error")
#
# finally:
#     print("FINALLY WILL ALWAYS RUN, ERROR OR NO ERROR")

# adding multiple acceptions in a try/catch allows you to better determine
# cause of error(s)

# Exercise
# Write a function called divider(a,b) that accepts two values a and b and returns
# the result a/b. Not that python throws an exception when b is zero. Write some
# error handling routine that prints "Please do not divide by zero!" if this
# ZeroDivisionError is raised

def divider(a,b):

    try:
        return a/b
    except ZeroDivisionError:
        print("Please do not divide by zero!")


#print(divider(1,2))
print(divider(1,0))

divider(1,0)


