"""Problem statement:
Using the sample file from the previous lesson create a python program that will do the following: 
•Create a python file that will use a terminal to allow a user to create a pizza.
•The program will present the user with a list available toppings for a pizza (based on the list of toppings given by the sample_data.txt from the previous assignment).
 The program will also list 3 “Chef Specialty Pizzas” which will be three custom pizzas of your choosing. 
•The program will ask the user to enter in their pizza order.
 If the user chooses 1-3, the program will display the chosen Specialty Pizza ingredients and display the price to the user. 
•If the user chooses a custom order, the program will do the following:
    o The program will ask the user for their desired toppings. 
    o If the user has requested a topping that is not on the list, the program will then ask the user if they would like to add that to the menu.
    o If the user requests yes, the program will then add that topping to the dictionary of toppings. The program will determine the price of the new topping based off of the average cost of the toppings currently available. The program will display the price of the requested pizza with all of the toppings. 
    o If the user requests no, the program will display the price of the pizza without the new topping, and show the price of the pizza and its ingredients to the user.


Solution by Author  : Sudha Sruthi Saravanan
Date                : 10th March 2013
Pre-requisite       : The file 'sample_data.txt' should be located in the directory path 'C:\Python27'.
"""



pizza_menu={}
sum_pizza_toppings=0
customer_choice=[]
sum_all_toppings=0
count=0

def bill():
    print "\n"
    print 50*'*'
    print "BILL"
    print 50*'*'
    print "{:<10}{:<30}{:<10}".format('S.no','Item','Cost')
    print 50*'*'
    
with open('sample_data.txt', 'r') as input:    
    for line in input:
        number,pizza_topping,price=(item.strip() for item in line.split(',',3))
        pizza_menu[pizza_topping]=price
    print 75*'*'
    print "Welcome to Pizza Hut @ JCI"
    print 75*'*'
    print "{:<10}{:<50}{:<10}".format('S.no','Item','Price')
    print 75*'*'
    print "\n{:<10}{:<50}{:<10}".format('1','COUNTRY FEAST','20')
    print "{:<10}{:<40}".format('',"(Corn,Mushroom, Tomato, Onion and Capsicum)")
        
    print "\n{:<10}{:<50}{:<10}".format('2','PANEER MAKHANI','21.5')
    print "{:<10}{:<40}".format('',"(Paneer,Capsicum,Onion and Green Chilles)")

    print "\n{:<10}{:<50}{:<10}".format('3','FIERY CHICKEN','22.5')
    print "{:<10}{:<40}".format('',"(Chicken,Capsicum,Onion and Green Chilles)")

    print "\n{:<10}{:<50}{:<10}".format('4','CUSTOM PIZZA','14+ price of topping')
    print "{:<10}{:<40}".format('',"(Pick the pizza topping of your choice)")
    print 75*'*'                    
    print "\nList of available Pizza toppings"
    print 35*'*'
    print "\n{:<20}{:<5}".format('Item','Price')
    for key, value in pizza_menu.items() :
        print "{:<20}{:<5}".format(key, value)
        sum_all_toppings=sum_all_toppings+float(value)
        count=count+1
    avg_all_toppings=round (sum_all_toppings/count,2)
    print 50*'*'
    print "Ordering begins : "
    print 50*'*' 
    print "Enter 1-3 to choose one of Chef's Speciality Pizza.\nIf your choice is a custom pizza enter 4."
    order=raw_input()
    if order=='1':
        print "Thank you for choosing COUNTRY FEAST.\n"
        bill()
        print "{:<10}{:<30}{:<10}".format('1','COUNTRY FEAST','20')
        print 50*'*'
        print "{:<10}{:<30}{:<10}".format('','Total','20')
        
    elif order=='2':
        print "Thank you for choosing PANEER MAKHANI.\n"
        bill()
        print "{:<10}{:<30}{:<10}".format('1','PANEER MAKHANI','21.5')
        print 50*'*'
        print "{:<10}{:<30}{:<10}".format('','Total','21.5')
    elif order=='3':
        print "Thank you for choosing FIERY CHICKEN.\n"
        bill()
        print "{:<10}{:<30}{:<10}".format('1','FIERY CHICKEN','22.5')
        print 50*'*'
        print "{:<10}{:<30}{:<10}".format('','Total','22.5')
        
    elif order=='4':
        print "\nFor choosing the topping the 'Item' of your choice."
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
                    print "Can this item be appended to the list of toppings?"
                    print "Enter Y if required and N if not required."
                    option=raw_input()
                    if option=='Y':
                        appended_text="\n"+"0"+","+choice+","+str(avg_all_toppings)
                        with open("sample_data.txt", "a") as myfile:
                            myfile.write(appended_text)
                        sum_pizza_toppings=sum_pizza_toppings+avg_all_toppings
                        customer_choice[len(customer_choice):]=[choice]
                        pizza_menu[choice]=avg_all_toppings
                        print "Thank you for suggesting to add "+choice+" to our menu. Please continue ordering."
                        choice=raw_input()
                    else:
                        print "Sorry we cannot add "+choice+" to our menu. Please continue ordering."
                        choice=raw_input()
                
        if len(customer_choice)==0:
            print "\nYou have not entered any choice!\nPlease re-run the program to choose a Pizza topping."
        elif len(customer_choice)!=1:
            print "\nThank you for choosing "+','.join(customer_choice[0:-1])+" and "+customer_choice[-1]+" pizza."
        else:
            print "\nThank you for choosing "+customer_choice[-1]+" pizza."
        bill()
        if sum_pizza_toppings!=0:
            count=0
            print "{:<10}{:<30}{:<10}".format('1','Base','14')
            for items in customer_choice:
                print "{:<10}{:<30}{:<10}".format(count+2,customer_choice[count],pizza_menu[customer_choice[count]])
                count=count+1
            pizza_price=14+sum_pizza_toppings
            print 50*'*'
            print "{:<10}{:<30}{:<10}".format('','Total',pizza_price)
            
    else:
        print "Please enter a number between 1-4 for an order."
print 50*'*'
            

        


  
    





