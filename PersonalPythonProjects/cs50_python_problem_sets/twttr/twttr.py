enter_text = input("Input: ")

for i in enter_text:
    vowel = i.lower()
    if vowel == "a":
        enter_text = enter_text.replace(i, "")
    elif vowel == "e":
        enter_text = enter_text.replace(i, "")
    elif vowel == "i":
        enter_text = enter_text.replace(i, "")
    elif vowel == "o":
        enter_text = enter_text.replace(i, "")
    elif vowel == "u":
        enter_text = enter_text.replace(i, "")
print(f"Output: {enter_text}")
