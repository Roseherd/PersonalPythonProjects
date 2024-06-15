def main():
    engraving = get_engraving()
    solid_gold = is_solid_gold()
    cost_of_project(engraving, solid_gold)


def get_engraving():
    engrave = input("Engraving: ")
    return engrave


def is_solid_gold():
    s_gold = input("Is your ring solid gold? ")
    boolean_s_gold = eval(s_gold)
    return boolean_s_gold


def cost_of_project(engraving, solid_gold):
    while not solid_gold:
        engraving_unit = 0
        for i in engraving:
            engraving_unit += 1
        project = 50 + (engraving_unit * 7)
        print(f"${project}")
        break
    while solid_gold:
        gold_engraving_unit = 0
        for i in engraving:
            gold_engraving_unit += 1
        gold_project = 100 + (gold_engraving_unit * 10)
        print(f"${gold_project}")
        break


if __name__ == "__main__":
    main()
