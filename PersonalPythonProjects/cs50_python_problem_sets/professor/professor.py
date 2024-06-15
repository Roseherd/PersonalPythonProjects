import random


def main():
    level = get_level()
    trial_limit = 3
    score = 0

    for _ in range(10):
        trial_count = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while trial_count < trial_limit:
            try:
                math_problem = int(input(f"{x} + {y} = "))
                trial_count += 1
                if math_problem == (x + y):
                    score += 1
                    break
                elif trial_count == trial_limit:
                    print("EEE")
                    print(f"{x} + {y} = {(x + y)}")
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    elif level == 3:
        number = random.randint(100, 999)
    else:
        raise ValueError
    return number


if __name__ == "__main__":
    main()
