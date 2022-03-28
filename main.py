from sys import exit

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
    "money": 0.0
}

# possible_choices = ["espresso", "latte", "cappuccino", "report"]
possible_choices = list(MENU.keys()) + ["report", "off"]

def main_func():
    global resources

    def report():
        print('')
        print(f"""Water: {resources["water"]}ml""")
        print(f"""Milk: {resources["milk"]}ml""")
        print(f"""Coffee: {resources["coffee"]}g""")
        print(f"""Money: ${resources["money"]}""")
        print("-----------------------------")

    def make_drink(drink_choice):
        for resource, amount in MENU[drink_choice]["ingredients"].items():
            resources[resource] -= amount

        report()
        print(f"Here is your {drink_choice}. Enjoy!")

    def insert_coin(coin_type):
        try:
            return int(input(f"How many {coin_type}? "))
        except ValueError:
            print("Unknown amount of coins. Try again!")
            return insert_coin(coin_type)

    try:
        choice = str(input("What would you like? ")).lower()
    except ValueError:
        print("Unknown command, try again!")
        main_func()

    if choice not in possible_choices:
        print("Unknown command, try again!")
        main_func()

    elif choice == "off":
        print("Turning off!")
        exit()

    elif choice == "report":
        report()
        # main_func()

    else:
        # resources_check = [resources[key] < value for key, value in MENU[choice]["ingredients"].items()]
        missing_ingredients = []
        for key, value in MENU[choice]["ingredients"].items():
            if resources[key] < value:
                missing_ingredients.append(key)

        if len(missing_ingredients) > 0:
            for ingredient in missing_ingredients:
                print(f"Sorry there is not enough {ingredient}.")
        else:
            print("Please insert coins.")
            number_of_quarters = insert_coin("quarters")
            number_of_dimes = insert_coin("dimes")
            number_of_nickles = insert_coin("nickles")
            number_of_pennies = insert_coin("pennies")
            inserted_money = round(
                number_of_pennies * 0.01 + number_of_nickles * 0.05 + number_of_dimes * 0.1 + \
                                 number_of_quarters * 0.25
            )

            if inserted_money < MENU[choice]["cost"]:
                print(f"Sorry that's not enough money. Amount of ${inserted_money} refunded.")

            elif inserted_money == MENU[choice]["cost"]:
                resources["money"] += inserted_money
                make_drink(choice)

            else:
                resources["money"] += MENU[choice]["cost"]
                make_drink(choice)
                print(f"""Here is ${inserted_money - MENU[choice]["cost"]} in change.""")


        # resources_check = [something for MENU[choice]["ingredients"]]
    main_func()


main_func()
