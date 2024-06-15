import sys
import csv
from tabulate import tabulate

table = []

if len(sys.argv) == 2:
    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    table.append([row[0], row[1], row[2]])
            print(tabulate(table, tablefmt="grid", headers="firstrow"))
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
