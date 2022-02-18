 # print("This is a test")

# lambda example:

seq = ['soup','dog','salad','cat','great']

# filter this list such that it only contains words that begin with the letter 's':


filteredList = list(filter(lambda word: word[0]=='s',seq))

print(filteredList)


# *You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results:
 # "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket".
 # If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
 # Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases. *

def speeding(speed, birthday):

    if birthday == True:
        speed -= 5
    elif speed <= 60:
         print("No Ticket")
    elif speed >= 61 & speed <= 80:
         print("Small Ticket")
    elif speed >= 81:
         print("Big Ticket")

#print(speeding(61, True))

