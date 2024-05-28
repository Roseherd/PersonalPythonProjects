import random


print(
    """In this guessing game the computer has a secret number and the player has \
to guess that number
Level is the upper limit of the range of numbers that the player will be guessing from.
Level must be 1,000,000 and above.
If you're wondering why level is so high, it's because this game is for geniuses.
If you think you can play then go ahead, but if not play an easier version lol.
But due to the game master's benevolence this genius game has been simplified.
You will get indications from the computer when you are close to the secret number.
Be grateful!😂
The player has an infinite number of tries in this guessing game.
Enjoy the guessing game :).
"""
)


def main():
    level = get_level()
    guess(level)


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


def guess(x):
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
            closeness1 = answer - num_guess_number
            if 70 < closeness1 <= 100:
                print("A bit close")
            elif 40 < closeness1 <= 70:
                print("Kinda close")
            elif 20 < closeness1 <= 40:
                print("Pretty close")
            elif 10 < closeness1 <= 20:
                print("Very close")
            elif 5 < closeness1 <= 10:
                print("Really, really close")
            elif 0 < closeness1 <= 5:
                print("OMG! Like, you're literally almost there. I'm surprised.😂")

        elif num_guess_number > answer:
            print("Sorry wrong guess! Guess was too high.")
            closeness2 = num_guess_number - answer
            if 70 < closeness2 <= 100:
                print("A bit close")
            elif 40 < closeness2 <= 70:
                print("Kinda close")
            elif 20 < closeness2 <= 40:
                print("Pretty close")
            elif 10 < closeness2 <= 20:
                print("Very close")
            elif 5 < closeness2 <= 10:
                print("Really, really close")
            elif 0 < closeness2 <= 5:
                print("OMG! Like, you're literally almost there. I'm surprised.😂")
    print(
        f"Yay, you correctly guessed the number {answer:,} after {guess_count} tries! :)"
    )


if __name__ == "__main__":
    main()
