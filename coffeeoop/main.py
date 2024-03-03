from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_is_on = True
while machine_is_on:
    coffee_options = menu.get_items()
    choice = input(f"What would you like to drink? {coffee_options}: ")
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_coffee = menu.find_drink(choice)
        if not coffee_maker.is_resource_sufficient(chosen_coffee):
            print("Sorry! Our ingredients are not sufficient to make your coffee.")
        if coffee_maker.is_resource_sufficient(chosen_coffee) and money_machine.make_payment(chosen_coffee.cost):
            coffee_maker.make_coffee(chosen_coffee)













