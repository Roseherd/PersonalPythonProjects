def main():
    engraving = get_engraving()
    solid_gold = is_solid_gold()
    cost_of_project(engraving, solid_gold)


def get_engraving():
    engrave = input("Engraving: ")
    return engrave


def is_solid_gold():
    s_gold = input("Is your ring solid gold(True or False)? ")
    boolean_s_gold = eval(s_gold)
    return boolean_s_gold


def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + (10 * len(engraving))) + (not solid_gold) * (50 + (7 * len(engraving)))
    print(f"${cost}")


if __name__ == "__main__":
    main()
