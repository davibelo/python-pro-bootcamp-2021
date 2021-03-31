from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# The Exercise consists to write Coffee Machine Code using given classes
# only reading classes documentation

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

status = True

while status:
    available_itens = menu.get_items()
    choice = input(f"What would you like? ({available_itens})")
    if choice == "off":
        status = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        if is_enough_ingredients:
            is_payment_successful = money_machine.make_payment(drink.cost)
            if is_payment_successful:
                coffee_maker.make_coffee(drink)
