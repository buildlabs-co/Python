from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drink_choice = Menu()
# report1 = CoffeeMaker()
# report2 = MoneyMachine()
# items = MenuItem("latte"["milk","espresso","cappuccino"],)
# consumer_choice = input(f"What would you like? ({drink_choice.get_items()}):")
# if consumer_choice == "report":
#     report1.report()
#     report2.report()
# elif consumer_choice == "espresso":
#     print(items.name)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"what is your order({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





