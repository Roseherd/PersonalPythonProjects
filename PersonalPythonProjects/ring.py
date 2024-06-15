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


cost_of_project("kobby", False)
