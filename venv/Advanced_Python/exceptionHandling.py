#errors and exception handling

# cannot 'catch' syntax error
#print("hello)

# example of catching a type error
try:
    print('10' + 10)

except IOError:
    print("You have an input/output error")
    print("Did you check the file permissions?")
except TypeError:
    print("You are using the wrong data types")

except:
    print("Hey you got an error")

finally:
    print("FINALLY WILL ALWAYS RUN, ERROR OR NO ERROR")

# adding multiple acceptions in a try/catch allows you to better determine
# cause of error(s)

