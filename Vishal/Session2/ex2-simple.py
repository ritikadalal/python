"""
author: vishal singh kushwaha
Purpose: This script parse data from text file into a list and a dictionary.
Concepts used:
                file I/O
                list and dictionary data types
                for loop
                Type casting
                List indexing and slicing
                operator overloading
                escape sequences
"""

# open the text file as file object in read only mode
f = open('sample_data.txt', 'r')

# create required variables
myList = []
myDict = {}
baseCost = 14.0

# read each line, remove '\n' and split string in a list using ', ' as a separator
# append first element of splitList as int to myList for every line in file
# use second element as a key and third element as value and add to myDict
for line in f:  # https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
    # print type(line)
    line = line.strip('\n')
    split = line.split(', ')
    myList.append(int(split[0]))
    myDict[split[1]] = float(split[2])

# close file to release system resources
f.close()

# print required output
# print myList
print 'Sum of column one is: ', sum(myList)
# print myDict
print 'Cost of sausage pizza with mushrooms, onions, and tomatoes is: ', str(
    baseCost + myDict['Sausage'] + myDict['Mushroom'] + myDict['Onion'] + myDict['Tomato'])
print 'Cost of pizza with olives, mushrooms, onions and corn is: ', str(
    baseCost + myDict['Olives'] + myDict['Mushroom'] + myDict['Onion'] + myDict['Corn'])
