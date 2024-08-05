MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

total_money = 0


def check_availability(coffee):
    """checks to see if there is enough of every ingredient"""
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print(f"Sorry, there is not enough water")
        return False
    elif coffee != "espresso" and resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        print(f"Sorry, there is not enough milk")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print(f"Sorry, there is not enough coffee")
        return False
    else:
        print(f"That will be ${MENU[coffee]["cost"]}. Please insert coins.")
        return True


def show_report():
    """shows a report of all resources in the coffee machine"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${total_money}")


def check_money():
    """checks for the amount of money given"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def alter_report(water, milk, coffee, cost):
    """updates the resource count in the coffee machine"""
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    global total_money
    total_money += cost


def refill():
    """refills the machine"""
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Refilled!")


def making_coffee(coffee):
    """receives money and makes coffee"""
    # getting details
    water_needed = MENU[coffee]["ingredients"]["water"]
    milk_needed = MENU[coffee]["ingredients"]["milk"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    cost = MENU[coffee]["cost"]

    if check_availability(coffee):
        money_given = check_money()
        if money_given > cost:
            print(f"You gave ${round(money_given, 2)}. Here is ${round((money_given - cost), 2)} in change.")
            print(f"Here is your {coffee} ☕. Enjoy!")
            alter_report(water_needed, milk_needed, coffee_needed, cost)
        elif money_given < cost:
            print("Insufficient coins. Money refunded")
        elif money_given == cost:
            print(f"Here is your {coffee} ☕. Enjoy!")
            alter_report(water_needed, milk_needed, coffee_needed, cost)


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        show_report()
    elif choice == "espresso":
        making_coffee("espresso")
    elif choice == "latte":
        making_coffee("latte")
    elif choice == "cappuccino":
        making_coffee("cappuccino")
    elif choice == "refill":
        refill()
    elif choice == "off":
        break
