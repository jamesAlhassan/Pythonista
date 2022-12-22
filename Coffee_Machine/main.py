menu = {
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
    "coffee": 100
}
money = 0


def is_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry! {item} not sufficient")
            return False
        return True


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif choice == "espresso":
        order = menu[choice]
        sufficient(order["ingredients"])
