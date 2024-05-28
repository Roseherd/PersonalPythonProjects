import random

game_over = False

while not game_over:
    while True:
        try:
            level = int(input("Select a Level: "))
            if level > 0:
                break
        except ValueError:
            pass
    answer = random.randint(1, level)
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {level}: "))
            if guess < 0:
                continue
            elif guess == answer:
                print("Just right!")
                game_over = True
                break
            elif guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
        except ValueError:
            pass
