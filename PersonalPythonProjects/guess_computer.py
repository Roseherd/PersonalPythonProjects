import random


print("""In this guessing game the computer has a secret number and the player has \
to guess that number
Level is the upper limit of the range of numbers that the player will be guessing from.
The player has an infinite number of tries in this guessing game.
Enjoy the guessing game :).
""")

def main():
    while True:
        try:
            level = int(input("Select a level: "))
            if level > 0:
                break
        except ValueError:
            pass
    guess(level)


def guess(x):
    answer = random.randint(1, x)
    guess_number = 0
    guess_count = 0
    while guess_number != answer:
        while True:
            try:
                guess_number = int(input(f"Guess a number between 1 and {x}: "))
                guess_count += 1
                if guess_number > 0:
                    break
                elif guess_number < 0:
                    continue
            except ValueError:
                pass
        if guess_number < answer:
            print("Sorry wrong guess! Guess was too low.")
        elif guess_number > answer:
            print("Sorry wrong guess! Guess was too high.")
    print(f"Yay, you correctly guessed the number {answer} after {guess_count} tries! :)")


if __name__ == "__main__":
    main()
