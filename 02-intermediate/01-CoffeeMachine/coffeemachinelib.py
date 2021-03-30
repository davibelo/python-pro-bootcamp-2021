MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 25,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def available_choices(menu):
    """Returns a list of available choices"""
    menu_itens = list(MENU.keys())
    maintainance_itens = ["off", "report"]
    result = menu_itens
    result.extend(maintainance_itens)
    return result


def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Ask to insert coins, return inserted total"""
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickels = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    inserted_money = quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    return inserted_money


def process_payment(drink, inserted_money):
    """Process payment, calculate change, returns profit"""
    cost = MENU[drink]["cost"]
    if inserted_money < cost:
        print("Sorry, not enough money. Money refunded: $" +
              str(('{:.2f}'.format(inserted_money))))
        return 0
    else:
        change = inserted_money - cost
        print("\nHere is your Change:$"+str(('{:.2f}'.format(change))))
        profit = cost
        return profit


def prepare_drink(ingredients):
    """Discount ingredients from resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
        # just checking that dictionary operations use values, not keys
        # item1 = resources[item]
        # item2 = ingredients[item]
        # print(f"resource: {item1}")
        # print(f"ingredient: {item2}")
