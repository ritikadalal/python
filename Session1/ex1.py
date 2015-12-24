"""
author: vishal singh kushwaha
version: 1.0
Purpose: This script takes person specific variables(of types string, float and list/tuple) and use them to print a
generalised introduction strings.
Concepts used:
                String concatenation
                Usage of .join(), .lower(), .upper(), .count(), round()
                Type casting
                List indexing and slicing
                PEP8 style guide for python code
                operator overloading
                escape sequences
"""

# binding required variables to person specific values
name = 'Vishal Singh Kushwaha'
food = ['Aloo Paratha', 'Pizza', 'Rajma Chawal']
color = 'Black'
service = 18.0/12
hobbies = ['Cricket', 'Driving', 'Music']

# intro_string1 concatenation using above variables
intro_string1 = 'Hello Everyone! My name is ' + name + '. My favorite foods are ' + ', '.join(food[0:-1]).lower() + \
                ' and ' + food[-1].lower() + '. My favorite color is ' + color.lower() + '.'

# intro_string2 concatenation using above variables
intro_string2 = 'I have worked at JCI for ' + str(round(service, 2)) + \
                " year(s). When I'm not working, my favorite things to do are " + ', '.join(hobbies[0:-1]).lower() + \
                ' and ' + hobbies[-1].lower() + '.'

# printing required output
print intro_string1,  intro_string2
print
# print 'Length of string 1: ' + str(len(intro_string1))
# print 'Length of string 2: ' + str(len(intro_string2))
print 'Total length of introduction: ', str(len(intro_string1 + intro_string2)), '\n'
print "Number of 'e's: ", str((intro_string1 + intro_string2).count('e')), '\n'
print 'Introduction in capital letters: \n', (intro_string1 + intro_string2).upper()
