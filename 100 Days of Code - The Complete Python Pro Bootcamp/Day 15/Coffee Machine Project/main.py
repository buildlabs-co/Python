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

money= 0

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(money,2)}")

def think(drink):
    global money
    print("Please insert coins.")
    quarter = int(input("how many quarters?: ")) * 0.25
    nickel = int(input("how many nickel?: ")) * 0.05
    dime = int(input("how many dimes?: ")) * 0.10
    penny = int(input("how many penny?: ")) * 0.01
    inserted_money = quarter + nickel + dime + penny
    cost = MENU[drink]["cost"]
    if inserted_money < cost:
        print("Sorry that's not enough money. Money refunded")
    else:
        change = inserted_money - cost
        money += cost
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {drink}. Enjoy!")

        drink_water = ((resources["water"]) - (MENU[drink]["ingredients"]["water"]))
        drink_coffee = ((resources["coffee"]) - (MENU[drink]["ingredients"]["coffee"]))
        if drink != "espresso":
            drink_milk = ((resources["milk"]) - (MENU[drink]["ingredients"]["milk"]))
            resources["milk"] = drink_milk

        resources["water"] = drink_water
        resources["coffee"] = drink_coffee
    return money


machine_ON = True
while machine_ON:
    drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink_choice == "report":
        report()

    elif drink_choice == "off":
        machine_ON = False

    elif drink_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        else:
            think("espresso")

    elif drink_choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        else:
            think("latte")

    elif drink_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        else:
            think("cappuccino")
