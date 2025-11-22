#weight = int(input("Enter Weight: "))

#if 0 <= weight <= 66:
    #print("you are flyweight")

#elif 66 <= weight <=73:
    #print("you are lightweight")

weight = int(input("Enter Weight: "))

weight_check = {
        "flyweight" : (0, 66),
        "lightweight": (66, 73),
        "light-middleweight": (73, 81), 
        "middleweight": (81, 90),
        "light-heavyweight": (90, 100),
        "heavyweight": (100, 1000)
        }

for weight_cat, (low, high) in weight_check.items():
    if low <= weight <= high: 
        print(f"You are {weight}(kg) which means you are {weight_cat}")

