print(""" V = titre volume of NaOH used in ml
Nap = Normal concentration of NaOH used (eg. 0.01 N)
F = Normality correction factor
meq-g = milliequivalent per gram of citric acid
Sample = Volume of the medicine used in ml (Volume used to prepare 10% solution)
NB: only enter numerical values without their units. 
""")

v = float(input("What's V? "))
nap = float(input("WHat's Nap? "))
f = float(input("What's F? "))
meqg = float(input("What's meq-g? "))
sample = float(input("What's Sample? "))

total_titratable_acidity = round(float((v * nap * f * meqg * 100) / sample), 2)


print(f"Acidity(%citric acid) = {total_titratable_acidity}")