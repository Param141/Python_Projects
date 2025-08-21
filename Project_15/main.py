from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
        

money_machine = MoneyMachine() # creating the object of MoneyMachine class to print the report through the function in the  class 
#money_machine.report() # printing the report of the money machine
menu = Menu() # creating the object of Menu class to print the report through the function in the class
is_on = True # variable to check if the machine is on or off

# object is named in the snake case  where all the letters are in lower case and words are separated by underscore
coffee_maker = CoffeeMaker() # creating the object of CoffeeMaker class to print the report
#coffee_maker.report() # printing the report of the coffee maker

# Read the documentation given in the course link to understand the Menu class and MenuItem class

while is_on: # while loop to check if the machine is on or off
    options = menu.get_items() # getting the items from the menu
    choice = input(f"What would you like? ({options}): ") # taking input from the user
    if choice == "off": # if the user enters off, the machine will be turned off
        is_on = False # setting the is_on variable to False
    elif choice == "report": # if the user enters report, the report of the coffee maker and money machine will be printed
        coffee_maker.report() # printing the report of the coffee maker
        money_machine.report() # printing the report of the money machine
    else: # if the user enters any other option
        drink = menu.find_drink(choice) # finding the drink from the menu
        if coffee_maker.is_resource_sufficient(drink): # checking if the resources are sufficient to make the drink
            if money_machine.make_payment(drink.cost): # checking if the payment is successful ( drink is the menu item object and each of the menu item obejct has access to three variables name,cost and ingredients)
                coffee_maker.make_coffee(drink) # making the coffee if payment is successful