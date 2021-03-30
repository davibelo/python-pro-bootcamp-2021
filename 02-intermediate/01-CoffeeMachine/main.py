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


def enough_resources(drink):
    """Check if exists enough resources for the drink"""
    if drink == "espresso":
        water_req = MENU[drink]["ingredients"]["water"]
        coffee_req = MENU[drink]["ingredients"]["coffee"]
        if water_req > resources["water"]:
            print("Sorry, not enough water")
            return False
        elif coffee_req > resources["coffee"]:
            print("Sorry, not enough coffee")
            return False
        else:
            return True
    else:
        water_req = MENU[drink]["ingredients"]["water"]
        milk_req = MENU[drink]["ingredients"]["milk"]
        coffee_req = MENU[drink]["ingredients"]["coffee"]
        if water_req > resources["water"]:
            print("Sorry, not enough water")
            return False
        elif milk_req > resources["milk"]:
            print("Sorry, not enough coffee")
            return False
        elif coffee_req > resources["coffee"]:
            print("Sorry, not enough coffee")
            return False
        else:
            return True


def process(drink):
    """Process payment, drink, calculate change"""
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickels = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    inserted_money = quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    cost = MENU[drink]["cost"]
    if inserted_money < cost:
        print("Sorry, not enough money. Money refunded: " +
              str(('{:.2f}'.format(inserted_money))))
    else:
        change = inserted_money - cost
        print("Get your "+drink+"... Change:$"+str(('{:.2f}'.format(change))))


def price(drink):
    """return drink price"""
    return MENU[drink]["cost"]


def recalculate_resources(drink):
    """Recalculate remain resources"""
    if drink == "espresso":
        water_req = MENU[drink]["ingredients"]["water"]
        coffee_req = MENU[drink]["ingredients"]["coffee"]
        resources["water"] -= water_req
        resources["coffee"] -= coffee_req
    else:
        water_req = MENU[drink]["ingredients"]["water"]
        milk_req = MENU[drink]["ingredients"]["milk"]
        coffee_req = MENU[drink]["ingredients"]["coffee"]
        resources["water"] -= water_req
        resources["milk"] -= milk_req
        resources["coffee"] -= coffee_req


money = 0
status = True
while status:
    choice = input("What would you like?(espresso/latte/cappuccino:")
    if choice == "off":
        status = False
    elif choice == "report":
        print("Water:" + str(resources["water"]) + "mL")
        print("Milk:" + str(resources["milk"]) + "mL")
        print("Coffee:" + str(resources["coffee"]) + "g")
        print("Money: $" + '{:.2f}'.format(money))
    elif choice == "espresso":
        resource_test = enough_resources(choice)
        if resource_test:
            process(choice)
            money += price(choice)
            recalculate_resources(choice)
    elif choice == "latte":
        resource_test = enough_resources(choice)
        if resource_test:
            process(choice)
            money += price(choice)
            recalculate_resources(choice)
    elif choice == "cappuccino":
        resource_test = enough_resources(choice)
        if resource_test:
            process(choice)
            money += price(choice)
            recalculate_resources(choice)
