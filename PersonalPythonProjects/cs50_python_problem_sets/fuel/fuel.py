while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        if int(x) > int(y):
            continue
        indication = float(int(x) / int(y)) * 100
        indication = round(indication)

        if indication <= 1:
            print("E")
        elif indication >= 99:
            print("F")
        else:
            print(f"{indication}%")
        break
    except (ValueError, ZeroDivisionError):
        pass







