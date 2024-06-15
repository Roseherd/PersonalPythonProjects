import sys


number_of_lines = 0
if len(sys.argv) == 2:
    try:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.strip() == "":
                        number_of_lines += 0
                    elif line.lstrip().startswith("#"):
                        number_of_lines += 0
                    else:
                        number_of_lines += 1
            print(number_of_lines)
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
