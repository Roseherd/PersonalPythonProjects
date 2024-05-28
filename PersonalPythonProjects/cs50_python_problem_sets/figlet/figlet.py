import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(random.choice(figlet.getFonts()))
    enter_text = input("Input: ")
    print(figlet.renderText(enter_text))
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:

    name_of_font = sys.argv[2]

    if (
        sys.argv[1] != "-f"
        and sys.argv[1] != "--font"
        or name_of_font not in figlet.getFonts()
    ):
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=name_of_font)
        enter_text = input("Input: ")
        print(figlet.renderText(enter_text))
