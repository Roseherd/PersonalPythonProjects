def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validity = True
    numeric_part = "".join([i for i in s if i.isdigit()])
    #LIst of unallowed punctuation marks
    unallowed_characters = [".", " ", ",", "!", ":", ";", "?", '"', "'"]
    #Initializing index of first_digit_index to -1
    first_digit_index = -1
    for i, value in enumerate(s):
        if value.isdigit():
            first_digit_index = i
            break
    #1.Condition for plate being between 2 and 6 characters
    if len(s) not in range(2, 7):
        validity = False
    #2.Condition for first two characters to be alphabets
    elif not s[0:2].isalpha():
        validity = False
    #3.Condition for number not to be in the middle of the plate
    elif first_digit_index != -1 and any(i.isalpha() for i in s[first_digit_index:]):
        validity = False
    #4.Condition for the number that is in the plate not to start with 0
    elif numeric_part.startswith("0"):
        validity = False
    #5.Condition for not allowing punctuation marks in the plate
    for i in s:
        if  i in unallowed_characters:
            validity = False
    return validity


if __name__ == "__main__":
    main()
