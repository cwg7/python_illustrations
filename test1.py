 # print("This is a test")

# lambda example:

seq = ['soup','dog','salad','cat','great']

# filter this list such that it only contains words that begin with the letter 's':


filteredList = list(filter(lambda word: word[0]=='s',seq))

print(filteredList)


