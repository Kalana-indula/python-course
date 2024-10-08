coffee_machine={
    "water":1000,
    "coffee":1000,
    "sugar":1000,
    "milk":1000,
    "money":100
}

print(coffee_machine["sugar"])
print(coffee_machine)

def report():
    print(
        f"Water :  {coffee_machine["water"]} ml \n"
        f"Milk : {coffee_machine["milk"]} \n"
        f"Sugar : {coffee_machine["sugar"]} \n"
        f"Coffee : {coffee_machine["coffee"]} \n"
        f"Money : {coffee_machine["money"]} \n"
    )

def get_user_input():
    input("Enter preferred type L for latte , E for espresso , C for cappacino ")
