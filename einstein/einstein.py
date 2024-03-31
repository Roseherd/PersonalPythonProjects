#Code to convert mass
def mass_converter():
    mass = int(input("m: "))
    print("E: ", energy(mass))


def energy(mass):
    speed_of_light = 300000000
    return mass * speed_of_light ** 2


mass_converter()
