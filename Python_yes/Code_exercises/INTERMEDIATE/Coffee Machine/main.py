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
    "water": 2000,
    "milk": 1000,
    "coffee": 500,
}

resources_money = 0
end_program = False


def report():
    print(f"water : {resources["water"]}ml")
    print(f"milk : {resources["milk"]}ml")
    print(f"coffee : {resources["coffee"]}gm")
    print(f"money : ${resources_money}")


def process_money():
    global coffee
    cost = coffee["cost"]
    coins_value = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25
    if coins_value < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = coins_value - cost
        if change > 0:
            print(f"Here is your ${change} change.")
        global resources_money
        resources_money += cost
        make_coffee()


def make_coffee():
    global coffee_ingredients
    global action
    for resource, amount in coffee_ingredients.items():
        resources[resource] -= amount
    print(f"Here is your {action}. Enjoy!")


print("COIN OPERATED COFFEE MACHINE\n\nWelcome!")

while not end_program:
    action = input("What would you like? espresso($1.5)/latte($2.5)/cappuccino($3) : ")
    if action == "report":
        report()
    elif action == "end":
        print("Goodbye.. have a great day!")
        end_program = True
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        flag = True
        coffee = MENU[action]
        coffee_ingredients = coffee["ingredients"]
        for key, value in coffee_ingredients.items():
            if value > resources[key]:
                flag = False
                print(f"Sorry, there isn't enough {key}.")
        if flag:
            print("Please enter your coins: ")
            pennies = int(input("pennies: "))
            nickels = int(input("nickels: "))
            dimes = int(input("dimes: "))
            quarters = int(input("quarters: "))
            process_money()
    else:
        print("Your prompt was invalid, please try again.")

