from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
money = MoneyMachine()
men = Menu()

# how to get cost
# drink.cost



coffee_order_one = True
while coffee_order_one is True:

    user = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if user == "report":
        coffee.report()
        money.report()
    
    elif user == "off":
        coffee_order_one = False

    elif user == "cappuccino" or user == "espresso" or user == "latte":
        drink = men.find_drink(user)
        if coffee.is_resource_sufficient(drink) is False:
            coffee_order_one = False
        elif money.make_payment(drink.cost) is True:
            coffee.make_coffee(drink)
                
