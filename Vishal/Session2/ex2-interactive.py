"""
author: vishal singh kushwaha
Purpose: This script is an interactive version of same problem statement. It takes topping options from user and process
          the input to do the calculations and print a bill.
Concepts used:
                file I/O
                list, set and dictionary data types
                for and while loop
                .format(), .keys(), .center() and .iteritems()
                Handing exceptions
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

# parse data in list and dictionary
for line in f:
    line = line.strip('\n')
    split = line.split(', ')
    myList.append(int(split[0]))
    myDict[split[1].lower()] = float(split[2])

# close file to release system resources
f.close()

print 'Sum of column one is: ', sum(myList), '\n'
print 'Cost of sausage pizza with mushrooms, onions, and tomatoes is: ', str(
    baseCost + myDict['sausage'] + myDict['mushroom'] + myDict['onion'] + myDict['tomato']), '\n'

# print Menu options in tabular form
print 'MENU OPTIONS'.center(24, '*')
print "{:<18} {:<5}".format('TOPPING', 'COST')  # https://docs.python.org/2/library/string.html#format-examples
for key, value in myDict.iteritems():
    print "{:<18} {:<5}".format(key, value)
print '*' * 24 + '\n'

# take user inputs, check for invalid inputs and handle wrong inputs
toppingCost = 0
while True:
    # toppingCost = 0
    ans = raw_input("Enter list of your toppings separated by ' '(a space) and press enter: ").lower()
    print '\n'
    if len(ans) == 0:  # if user selects no options give message
        print 'Enter at least one topping'
    else:
        # try:  # if user makes a choice which is not a key in dictionary, appropriate message should be displayed
            ans = ans.split(' ')
            if set(ans) < set(myDict.keys()):  # print header only if user input is a subset of keys in dictionary
                print 'BILL'.center(24, '*')
                for item in ans:
                    toppingCost += myDict[item]
                    print "{:<18} {:<5}".format(item, myDict[item])
                break
            else:
                print 'Invalid input, typo found'
        # except KeyError:  # https://docs.python.org/2/tutorial/errors.html#handling-exceptions
            # print 'Invalid input, typo found'

print "{:<18} {:<5}".format('Base cost ', str(baseCost))
print '*' * 24
print "{:<18} {:<5}".format('Total cost: ', str(baseCost + toppingCost))
print '*' * 24 + '\n'
