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
    "water": {
        "val": 300,
        "unit": "ml",
    },
    "milk": {
        "val": 200,
        "unit": "ml",
    },
    "coffee": {
        "val": 76,
        "unit": "g",
    },
}

coins_counts = {
    "quarters": 0,
    "dimes": 5,
    "nickles": 5,
    "pennies": 5,
}

COIN_VALUE = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}

LOGO = '''
      )  )  )
     (  (  (        Coffee Machine
 .-'---------|      ---------------------
( C|/\/\/\/\/|      * Espresso    $1.5
 '-./\/\/\/\/|      * Latte       $2.5
   '_________'      * Cappuccino  $3.0
    '-------'
'''

def print_resources():
    for key in resources.keys():
        print(f"{key}: {resources[key]['val']}{resources[key]['unit']}")
    amount = 0
    for coin, count in coins_counts.items():
        print(f"{coin}: {count}")
        amount += COIN_VALUE[coin] * coins_counts[coin]
    print(f"(Money: ${amount: .2f})")


def check_resources(order):
    for key in MENU[order]["ingredients"].keys():
        if resources[key]["val"] < MENU[order]["ingredients"][key]:
            print(f"Sorry, there is not enough {key}.")
            return False

    return True


def update_resources(order):
    for key in MENU[order]["ingredients"].keys():
        resources[key]["val"] -= MENU[order]["ingredients"][key]


def check_pay(pay, order):
    global coins_counts
    payment = 0
    for coin in pay.keys():
        payment += float(COIN_VALUE[coin]) * int(pay[coin])

    if payment < MENU[order]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif payment == MENU[order]["cost"]:
        for coin in pay.keys():
            coins_counts[coin] += int(pay[coin])
    elif payment > MENU[order]["cost"]:
        new_coins_counts = {}
        for coin in pay.keys():
            new_coins_counts[coin] = int(coins_counts[coin]) + int(pay[coin])

        change = round(payment - MENU[order]["cost"], 2)
        change_coins = {}
        if get_change(change, new_coins_counts, change_coins):
            coins_counts = new_coins_counts
            print_change(payment - MENU[order]["cost"], change_coins)
        else:
            print("Sorry, we're currently out of change. Money refunded.")
            return False

    return True


def get_change(amount, available_coins_counts, change_coins):
    for coin in available_coins_counts.keys():
        # print(f"{coin}, amount is {amount}")
        while amount >= COIN_VALUE[coin] and available_coins_counts[coin] > 0:
            amount = round(amount - COIN_VALUE[coin], 2)
            change_coins[coin] = change_coins.get(coin, 0) + 1
            available_coins_counts[coin] -= 1

    if amount == 0:
        return True
    else:
        return False


def print_change(amount, change_coins):
    print(f"Here is the {amount:.2f} in change:")
    for key, value in change_coins.items():
        print(key, value)


print(LOGO)
on_business = True
while(on_business):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "exit":
        on_business = False
        continue
    elif choice == "report":
        print_resources()
        continue
    elif choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print("Invalid input. Please select espresso/latte/cappuccino.")
        continue

    if not check_resources(choice):
        continue

    print("Please insert coins.")
    pay = {}
    for coin in COIN_VALUE.keys():
        pay[coin] = input(f"how many {coin}s?: ")

    if check_pay(pay, choice):
        update_resources(choice)
        print(f"Here is your {choice} ☕️. Enjoy! \n")
