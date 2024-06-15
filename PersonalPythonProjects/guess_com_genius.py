import random


print(
    """In this guessing game the computer has a secret number and the player has \
to guess that number
Level is the upper limit of the range of numbers that the player will be guessing from.
Level must be 1,000,000 and above.
If you're wondering why level is so high, it's because this game is for geniuses.
If you think you can play then go ahead, but if not play an easier version lol.
The player has an infinite number of tries in this guessing game.
Enjoy the guessing game :).
"""
)


def main():
    name = get_name()
    level = get_level()
    guess(level, name)


def get_name():
    name = input("Enter your name: ")
    return name


def get_level():
    while True:
        try:
            level = input("Select a level: ")
            if "," in level:
                modified_level = level.replace(",", "")
                num_level = int(modified_level)
                if num_level >= 1000000:
                    return num_level
            else:
                num_level = int(level)
                if num_level >= 1000000:
                    return num_level

        except ValueError:
            pass


def guess(x, name):
    answer = random.randint(1, x)
    num_guess_number = 0
    guess_count = 0
    while num_guess_number != answer:
        while True:
            try:
                guess_number = input(f"Guess a number between 1 and {x:,}: ")
                if "," in guess_number:
                    modified_guess_number = guess_number.replace(",", "")
                    num_guess_number = int(modified_guess_number)
                    guess_count += 1
                    if num_guess_number > 0:
                        break
                    elif num_guess_number < 0:
                        continue
                else:
                    num_guess_number = int(guess_number)
                    if num_guess_number > 0:
                        break
                    elif num_guess_number < 0:
                        continue

            except ValueError:
                pass
        if num_guess_number < answer:
            print("Sorry wrong guess! Guess was too low.")
        elif num_guess_number > answer:
            print("Sorry wrong guess! Guess was too high.")
    print(
        f"Congratulations {name}! You have correctly guessed the number {answer:,} after {guess_count} tries! 🥳"
    )


if __name__ == "__main__":
    main()
