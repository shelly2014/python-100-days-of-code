import sys
sys.path.append('../../OOP-Coffee-Machine/oop-coffee-machine-solution/oop-coffee-machine-solution')

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

LOGO = '''
      )  )  )
     (  (  (        Coffee Machine
 .-'---------|      ---------------------
( C|/\/\/\/\/|      * Espresso    $1.5
 '-./\/\/\/\/|      * Latte       $2.5
   '_________'      * Cappuccino  $3.0
    '-------'
'''

print(LOGO)
on_business = True
while(on_business):
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "exit":
        on_business = False
        continue
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if not coffee_maker.is_resource_sufficient(drink):
            continue

        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
