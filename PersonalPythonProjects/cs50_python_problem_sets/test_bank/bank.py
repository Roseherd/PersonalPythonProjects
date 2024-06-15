def main():
    kind_of_greeting = input("Greeting: ")
    print(f"${value(kind_of_greeting)}")


def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        amount = 0
    elif greeting.startswith("h"):
        amount = 20
    else:
        amount = 100
    return amount


if __name__ == "__main__":
    main()
