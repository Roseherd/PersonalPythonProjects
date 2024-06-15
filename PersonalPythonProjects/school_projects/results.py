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
                    table.append(row)  # Append the entire row instead of just the first three columns
            print(tabulate(table, tablefmt="grid", headers="firstrow"))
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
