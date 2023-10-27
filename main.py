MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# def RemainItems(drink):
#
#
#     Remaining_water = resources["water"]-MENU[str(drink)]["ingredients"]["water"]
#     # print(f"Remaining_water = {Remaining_water}")
#
#     Remaining_milk = resources["milk"]-MENU[str(drink)]["ingredients"]["milk"]
#     # print(f"Remaining_milk = {Remaining_water}")
#
#     Remaining_coffee = resources["coffee"]-MENU[str(drink)]["ingredients"]["coffee"]
#     return Remaining_water, Remaining_milk , Remaining_coffee
#
#
#
#
# def Calculations(drink,Full_Amount, water,milk,coffee):
#
#     if Full_Amount >= Tolal_Amount[str(drink)]:
#          print("Okay")
#
#     elif drink == 'report':
#         print(f"Remaining water : {water}")
#         print(f"Remaining water : {milk}")
#         print(f"Remaining water : {coffee}")
#
#     else:
#         print("not enough money.!!!")
#
# Tolal_Amount = {"espresso" : 1.5,
#                 "latte": 2.5,
#                 "cappucino" : 3}
#
#
#
#
#
# Choise = input("What would you like? (espresso/latte/cappuchino) : ").lower()
# # print(Choise)
# water , milk , coffee = RemainItems(Choise)
#
# if Choise == "report":
#     print(f"Remaining water : {water}")
#     print(f"Remaining water : {milk}")
#     print(f"Remaining water : {coffee}")
# else:
#
#     print("Please insert coins. ")
#     quarters_amount = int(input("How many quarters ? : "))
#     dimes_amount = int(input("How many quarters ? : "))
#     nickles_amount = int(input("How many quarters ? : "))
#     pennies_amount = int(input("How many quarters ? : "))
#     Full_Amount = quarters_amount * 0.25 + dimes_amount * 0.1 + nickles_amount*0.05 + pennies_amount*0.01
#     Calculations(Choise,Full_Amount,water,milk,coffee)






def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough =  False
    return is_enough



def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters ? : "))*0.25
    total += int(input("How many quarters ? : "))*0.1
    total += int(input("How many quarters ? : "))*0.05
    total += int(input("How many quarters ? : "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted or return False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} Changes")
        global  profit
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def make_coffee(drink_name,order_ingrediance):
   for item in order_ingrediance:
       resources[item] -= order_ingrediance[item]
   print(f"Here is your {drink_name} ")



from logo import art

print(art)

is_on = True

while is_on :
    Choise = input("What would you like? (espresso/latte/cappuchino) : ").lower()
    if Choise == "off":
        is_on = False

    elif Choise == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}.")

    else:
        drink = MENU[Choise]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(Choise, drink["ingredients"])



