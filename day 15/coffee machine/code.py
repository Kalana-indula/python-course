coffee_machine={
    "water":1000,
    "coffee":1000,
    "sugar":1000,
    "milk":1000,
    "money":100
}

espresso={
    "water":200,
    "coffee":50,
    "sugar":20,
    "milk":0,
    "price":2
}

latte={
    "water":150,
    "coffee":50,
    "sugar":20,
    "milk":20,
    "price":4
}

cappuccino={
    "water": 150,
    "coffee": 50,
    "sugar": 20,
    "milk": 50,
    "price": 4
}

def make_espresso():
    coffee_machine["water"]-=espresso["water"]
    coffee_machine["sugar"]-=espresso["sugar"]
    coffee_machine["coffee"]-=espresso["coffee"]
    coffee_machine["milk"]-=espresso["milk"]
    coffee_machine["money"]+=espresso["price"]

def make_cappuccino():
    coffee_machine["water"]-=cappuccino["water"]
    coffee_machine["sugar"]-=cappuccino["sugar"]
    coffee_machine["coffee"]-=cappuccino["coffee"]
    coffee_machine["milk"]-=cappuccino["milk"]
    coffee_machine["money"]+=cappuccino["price"]

def make_latte():
    coffee_machine["water"] -= latte["water"]
    coffee_machine["sugar"] -= latte["sugar"]
    coffee_machine["coffee"] -= latte["coffee"]
    coffee_machine["milk"] -= latte["milk"]
    coffee_machine["money"] += latte["price"]

def report():
    print(
        f"Water :  {coffee_machine["water"]} ml \n"
        f"Milk : {coffee_machine["milk"]} \n"
        f"Sugar : {coffee_machine["sugar"]} \n"
        f"Coffee : {coffee_machine["coffee"]} \n"
        f"Money : $ {coffee_machine["money"]} \n"
    )

# getting user inputs
def get_user_input():
    type=input("Enter preferred type L for latte , E for espresso , C for cappuccino ")
    return type.lower()

def buy_coffee():
    coffee_type=get_user_input()
    if(coffee_type=='c'):
        make_cappuccino()
    elif(coffee_type=='l'):
        make_latte()
    elif(coffee_type=='e'):
        make_espresso()
    else:
        print("Enter valid type")

    print(coffee_machine)

while(True):
    buy_coffee()
    power=input("Press 'Off' for turn off the machine : ")

    if(power=="Off"):
        break
