import sys
import csv


students = []
new_students = []
if len(sys.argv) == 3:
    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], newline="") as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    students.append({"name" : row["name"], "house" : row["house"]})
            for student in students:
                last, first = student["name"].split(", ")
                new_students.append({"first" : first, "last" : last, "house" : student["house"]})
            with open(sys.argv[2], "w",newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for n_student in new_students:
                    writer.writerow({"first": n_student["first"], "last" : n_student["last"], "house" : n_student["house"]})
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
