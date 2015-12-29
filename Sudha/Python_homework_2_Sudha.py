"""Problem statement:
Retrieve data from a file "sample_data.txt" using Python and Python File I/O.
Parse/Save the data in the file into these formats:
Save the first column of data into a list.
Save the second and third columns as key-value pairs in a dictionary
with the second column as the key and the third column as the value.
1, 2, 3
4, 5, 6
Compute the sum of the elements of the first column.
Using the dictionary, compute the sum of a pizza with various toppings.

Solution by Author  : Sudha Sruthi Saravanan
Date                : 1st March 2013
Pre-requisite       : The file 'sample_data.txt' should be located in the directory path 'C:\Python27'.
"""

list_numbers=[]
sum_of_numbers=0
pizza_menu={}
sum_pizza_toppings=0
customer_choice=[]
with open('sample_data.txt', 'r') as input:
    
    for line in input:
        number,pizza_topping,price=(item.strip() for item in line.split(',',3))
        list_numbers[len(list_numbers):]=[number]
        pizza_menu[pizza_topping]=price
        sum_of_numbers=sum_of_numbers+int(number)
    print "First column of data from sample_data in a list format:\n\n"+str(list_numbers)
    print "\nSum of Numbers of first column : "+str(sum_of_numbers)
    print 
    print "\nMenu of Pizza toppings"
    print "\n{:<20}{:<5}".format('Item','Price')

    for key, value in pizza_menu.items() :
        print "{:<20}{:<5}".format(key, value)
    sausage_pizza_price=14+float(pizza_menu['Sausage'])+float(pizza_menu['Mushroom'])+float(pizza_menu['Onion'])+float(pizza_menu['Tomato'])
    print "\nPrice of a Sausage Pizza with  mushrooms, onions, and tomatoes is "+str(sausage_pizza_price)
   
    print "\nFor choosing your favorite pizza and topping type the 'Item' of your choice."
    print "Press 'Enter' key after entering the first 'Item' of choice"
    print "Type 'Done' if you have completed the order\n"
    choice=raw_input()
    while choice!='Done':
        if choice!='Done':
            try:
                sum_pizza_toppings=sum_pizza_toppings+float(pizza_menu[choice])
                customer_choice[len(customer_choice):]=[choice]
                choice=raw_input()               
            except KeyError:
                print "Please enter the items in the menu or 'Done' if the order is completed"
                choice=raw_input() 
    if len(customer_choice)==0:
        print "\nYou have not entered any choice!\nPlease re-run the program to choose a Pizza topping."
    elif len(customer_choice)!=1:
        print "\nCustomer's choice is "+','.join(customer_choice[0:-1])+" and "+customer_choice[-1]+"."
    else:
        print "\nCustomer's choice is "+customer_choice[-1]+"."
    if sum_pizza_toppings!=0:
        print "Base Cost of Pizza is 14"
        print "Price of the topping combination is "+str(sum_pizza_toppings)
        pizza_price=14+sum_pizza_toppings
        print "Total Cost of Pizza is "+ str(pizza_price)

        
    
        
    





