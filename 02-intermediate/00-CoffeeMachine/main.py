import coffeemachinelib as cml

status = True

while status:
    choice = input("What would you like?(espresso/latte/cappuccino:")
    valid_choices = cml.available_choices(cml.MENU)
    if choice in valid_choices:
        if choice == "off":
            status = False
        elif choice == "report":
            print("Water:" + str(cml.resources["water"]) + "mL")
            print("Milk:" + str(cml.resources["milk"]) + "mL")
            print("Coffee:" + str(cml.resources["coffee"]) + "g")
            print("Money: $" + '{:.2f}'.format(cml.money))
        else:
            drink = cml.MENU[choice]
            if cml.enough_resources(drink["ingredients"]):
                total_inserted = cml.process_coins()
                cml.money += cml.process_payment(choice, total_inserted)
                cml.prepare_drink(drink["ingredients"])
                print(f"Get your {choice}...")

    else:
        print("Error: Invalid choice. Try again")
