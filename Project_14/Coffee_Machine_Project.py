MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0 # to show the total money owned by the coffee machine 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit # this is acting in local scope but profit is outside in global scope
        # so we need to use global keyword to modify the global variable
        profit += drink_cost # update the profit with the cost of the drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off": # Turn off the coffee machine
        is_on = False
    elif choice == "report": # Print a report of the current resources and profit
        print("Current resources:") # print all the current values of resources
        print(f"Water: {resources['water']}ml") # already have outer double qoutes that's why used single qoutes inner side 
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice] # user chooses a drink from the menu
        if is_resource_sufficient(drink["ingredients"]): #first check if there are enough resources
            # if there are enough resources then process the coins
            payment = process_coins() # total amount of coins inserted by the user
            # check if the payment is successful 
            if is_transaction_successful(payment, drink["cost"]): # if payment is enough to buy the drink
                # if payment is successful then make the coffee
                make_coffee(choice, drink["ingredients"]) 
# first accessing a specific drink from the MENU dictionary then its order_ingredients







# This code is a simple coffee machine program that allows users to order coffee drinks.
# It checks if there are enough resources, processes the payment, and makes the coffee if everything