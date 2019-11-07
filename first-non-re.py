###############################################
# This programme returns the first non-repeated
# character of the string specified by user.
###############################################

# Read input from console
s = input("Enter a string: ")

# Initialise the degree of distinction. Each time
# we compare a character to another one in the
# string, if the two are not the same then distinct
# increases by 1. In the end, ask if the character
# has distinct=len(string). If yes then print the
# character and exit.

distinct = 0 

for i in len(s):
    character = s[i]
    for j in len(s):
        #break on the first re-occurence of character
        if character = s[j]:
            break
        else:
            distinct = distinct + 1

    if distinct = len(s) :
        print("The first non-repeated character in your string is: {}".format(character))
        break
        
