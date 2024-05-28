import inflect

p = inflect.engine()

names = []

while True:
    try:
        enter_name = input("Name: ")
        names.append(enter_name)
    except EOFError:
        print()
        break

name_list = p.join((names))
print(f"Adieu, adieu, to {name_list}")
