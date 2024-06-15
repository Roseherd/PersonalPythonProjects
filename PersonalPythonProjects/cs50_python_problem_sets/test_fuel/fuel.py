def main():
    fraction = input("Fraction: ")
    print(convert(fraction))
    print(gauge(convert(fraction)))


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError



    percentage = float(int(x) / int(y)) * 100
    percentage = round(percentage)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        reading = "E"
    elif percentage >= 99:
        reading = "F"
    else:
        reading = f"{percentage}%"
    return reading


if __name__ == "__main__":
    main()



