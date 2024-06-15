import random


print(
    """In this guessing game the player has a secret number and the computer \
has to guess that secret number. 
Upper bound is the upper limit of the range from the number 1 of the range of values \
that the computer will guess from.
In order to play, your secret number must be within the specified range selected.
Enjoy the guessing game :).
"""
)


def main():
    high = get_high()
    computer_guess(high)


def get_high():
    while True:
        try:
            high = input("Select an upper bound: ")
            if "," in high:
                modified_high = high.replace(",", "")
                num_high = int(modified_high)
                return num_high
            else:
                num_high = int(high)
                return num_high
        except ValueError:
            pass


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess_count = 0
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess:,} too high(H), too low(L) or correct(C): "
        ).lower()
        guess_count += 1
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(
        f"Computer guessed the number {guess:,} correctly after {guess_count} tries. :)"
    )


if __name__ == "__main__":
    main()
