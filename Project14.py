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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def subtract_mon(a,b):
    diff = a - b
    return diff

def process_coins(a,b,c,d):
    e = a+b+c+d
    return e

def select_item(random):
    items_one = {}
    if random in MENU:
        items_one = {key: MENU[random]["ingredients"][key] for key in MENU[random]["ingredients"]}
    return items_one

def check_resource(a):
    items_two = {key: a[key] for key in a}
    return items_two

def subtract_resource(a,b):
    resources_adj = {key: a[key]- b.get(key, 0) for key in a}
    return resources_adj

def compare_resources(a,b):
    not_enough = []
    for key in a:
        if a[key] < b.get(key, 0):
            not_enough.append(key)
    return not_enough



profit = 0
change_act = 0
money = 0

def order(user_1):
    global profit
    profit = MENU[user_1]["cost"]
    return profit



coffee_order_one = True
while coffee_order_one is True:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user == "cappuccino" or user == "latte" or user == "espresso":
        print("Please insert coin.")
        quart = 0.25 * float(input("How many quarters: "))
        dime = 0.10 * float(input("How many dimes: "))
        nick = 0.05 * float(input("How many nickels: "))
        penn = 0.01 * float(input("How many pennies: "))

        money = round(process_coins(quart, dime, nick, penn), 2)
        order(user)

        if user == "cappuccino":
            if compare_resources(check_resource(resources), select_item(user)):
                    print(f"Sorry, there is not enough {compare_resources(check_resource(resources), select_item(user))}")
                    print(f"Money refunded {money} ")
                    exit()
            elif money >=  MENU[user]["cost"]:
                change = round(subtract_mon(money, MENU[user]["cost"]),2)
                change_act += change
                print(f"Here is your {change} in change.")
                print(f"Here is your {user}. Enjoy!")
            elif money < MENU[user]["cost"]:
                print(f"Sorry that's not enough money. Money refunded {money} ")
        elif user == "espresso":
            if compare_resources(check_resource(resources), select_item(user)):
                    print(f"Sorry, there is not enough {compare_resources(check_resource(resources), select_item(user))}")
                    print(f"Money refunded {money} ")
                    exit()
            elif money >= MENU[user]["cost"]:
                change = round(subtract_mon(money, MENU[user]["cost"]), 2)
                change_act += change
                print(f"Here is your {change} in change.")
                print(f"Here is your {user}. Enjoy!")
            elif money < MENU[user]["cost"]:
                print(f"Sorry that's not enough money. Money refunded {money} ")
        else:
            if compare_resources(check_resource(resources), select_item(user)):
                    print(f"Sorry, there is not enough {compare_resources(check_resource(resources), select_item(user))}")
                    print(f"Money refunded {money} ")
                    exit()
            elif money >= MENU[user]["cost"]:
                change = round(subtract_mon(money, MENU[user]["cost"]), 2)
                change_act += change
                print(f"Here is your {change} in change.")
                print(f"Here is your {user}. Enjoy!")
            elif money < MENU[user]["cost"]:
                print(f"Sorry that's not enough money. Money refunded {money} ")

        resources = subtract_resource(check_resource(resources), select_item(user))

    elif user == "report":
        for k, v in resources.items():
            print(k, v)
        print(f"Money: ${round(profit,1)}")

    elif user == "off":
        exit()

