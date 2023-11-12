import data

Menu = data.MENU
profit = 0
Resources = data.resources


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, and False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= Resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated form coins inserted"""
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * .25
    total += float(input("How many dimes?: ")) * .1
    total += float(input("How many nickles?: ")) * .05
    total += float(input("How many pennies?: ")) * .01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Returns Trues when the payment is accepted, or False if money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        Resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {Resources['water']} ml")
       print(f"Milk: {Resources['milk']}ml")
       print(f"Coffee: {Resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = Menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment =  process_coins()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice,drink["ingredients"])






