enter_text = input("Input: ")

replace_dict = {"a" : "", "e" : "", "i" : "", "o" : "", "u" : ""}

for old,new in replace_dict.items():
    enter_text = enter_text.replace(old, new)

print(f"Output: {enter_text}")
