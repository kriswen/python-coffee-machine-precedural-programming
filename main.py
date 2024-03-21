# Coffee Machine
from art import logo

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
    "water": 500,
    "milk": 500,
    "coffee": 100,
}


# TODO: 1.print report
def print_report():
    """print the report of ingredients and money received"""
    print("#####################################")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(money_available, 2)}")
    print("#####################################")


# TODO: 2. check resources sufficient?
def check_resources(coffee):
    """take a drink type and return insufficient resources (if any) in a list"""
    depleted_resources = []
    ingredients_needed = MENU[coffee]["ingredients"]
    # print(ingredients_needed)
    for key, value in ingredients_needed.items():
        # print(f"need: {key} {value}")
        # print(f"resource for {key}: {resources[key]}")
        # add ingredient name to depleted list if not sufficient
        if int(resources[key]) < value:
            depleted_resources.append(key)
    # print(f"depleted list: {depleted_resources}")
    return depleted_resources


# TODO: 3. process coins
def process_coins():
    """prompt user to insert coins, and return total dollar received"""
    print("please insert coins.")
    quarters = float(input("How many quarters?: ") or 0)
    dimes = float(input("How many dimes?: ") or 0)
    nickels = float(input("How many nickels?: ") or 0)
    pennies = float(input("How many pennies?: ") or 0)
    total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    return total_amount


# TODO: 4. check transaction successful?
def check_transaction(money, coffee):
    """Take the money and drink as input, and return True/False if it can cover the cost"""
    drink_cost = MENU[coffee]["cost"]
    print(f"The {coffee} cost ${drink_cost} and we received ${money} from you.")
    return money >= drink_cost


# TODO: 5. make coffee
def make_coffee(coffee):
    # deduct ingredients from the resources
    ingredients_needed = MENU[coffee]["ingredients"]
    for key, value in ingredients_needed.items():
        resources[key] -= value
        # print(f"deducting {value} of {key}")
    # print the coffee
    print(f"Here is your {coffee} ☕, enjoy!")


def print_logo_menu():
    """function that prints logo and menu from MENU dictionary"""
    print(logo)
    print("MENU: ", end="")
    for key, value in MENU.items():
        coffee_name = key
        cost = value["cost"]
        print(f"{coffee_name} ${cost}", end="  ")
    print("\n")


# set initial values
money_available = 0.00
coffee_machine_on = True
print_logo_menu()
# Main program run
# TODO: prompt user for input (options: expresso, latte, cappuccino, report, off)

while coffee_machine_on:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print_report()
    elif user_input == "off":
        # turn off coffee machine (exit out the program)
        print("Coffee machine is turning off...")
        coffee_machine_on = False
    elif user_input == "expresso" or "latte" or "cappuccino":
        coffee_type = user_input
        # check if depleted_resource list is empty
        if not check_resources(coffee_type):
            # process coins if sufficient resources
            money_received = round(process_coins(), 2)
            # check if money is enough to cover the drink cost
            if check_transaction(money_received, coffee_type):
                # process refund for the extra money received
                refund_amount = round(money_received - MENU[coffee_type]["cost"], 2)
                if refund_amount > 0:
                    print(f"Here is ${refund_amount} dollars in change.")
                # bank the money if money is enough to cover the cost of drink & refund processed
                money_after_refunded = money_received - refund_amount
                money_available += round(money_after_refunded, 2)
                # make the coffee
                make_coffee(coffee_type)
            else:
                print("Sorry that's not enough money. Money refunded.")

        # if there is any insufficient resource, list them out
        else:
            depleted_items = " & ".join(check_resources(coffee_type))
            print(f"Sorry there is not enough {depleted_items}.")
