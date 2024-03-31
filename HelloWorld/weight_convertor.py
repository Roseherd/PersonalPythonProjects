#Ask for user's weight
weight = input("Weight: ")
unit_of_weight = input("(L)bs or (K)g: ").lower()
if unit_of_weight == "l":
    weight_in_kilos = float(weight) * 0.45
    print(f"You are {weight_in_kilos} kilos")
elif unit_of_weight == "k":
    weight_in_pounds = float(weight) / 0.45
    print(f"You are {weight_in_pounds} pounds")

