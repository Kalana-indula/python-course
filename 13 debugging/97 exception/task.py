try:
    age=int(input("How old are you ?"))
except ValueError:
    print("Wron type")
    age=int(input("How old are you ?"))

if(age>18):
    print(f"You can drive at {age}")