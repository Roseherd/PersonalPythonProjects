def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    for i in word:
        vowel = i.lower()
        if vowel == "a":
            word = word.replace(i, "")
        elif vowel == "e":
            word = word.replace(i, "")
        elif vowel == "i":
            word = word.replace(i, "")
        elif vowel == "o":
            word = word.replace(i, "")
        elif vowel == "u":
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
