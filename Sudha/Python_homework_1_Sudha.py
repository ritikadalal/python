name='Sudha'
color='orange'
food=['citrus fruits', 'shakes', 'chettinad fish fry ']
years=3.5
foodlen =len(food)
hobbies=['blogging','painting hand made cards','reading fiction']
intro_string="\nHello Everyone! My name is "+name+".\n"+"My favorite foods are "+food[0]+","+food[1]+ " and "+food[-1]+".\n"+"My favorite color is "+color+"."
print intro_string
intro_string_2="\nI have worked at JCI for "+str(years)+" years.\nWhen I am not working, my favorite things to do are "+hobbies[0]+","+hobbies[1]+" and "+hobbies[-1]+"."
print intro_string_2
single_intro_string=intro_string+intro_string_2
print "\nLength of the intro string is "+ str(len(single_intro_string))
print "\nNumber of e's in the intro string is " + str(single_intro_string.count('e'))
print "\nIntroduction in capital letters: \n" + (single_intro_string).upper()
