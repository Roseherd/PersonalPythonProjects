courses = {
    "SPC 151": 4,
    "SPC 181": 4,
    "SPC 161": 4,
    "MATH 111": 1,
    "URC 141": 1,
    "URC 143": 1,
    "SPC 152": 4,
    "SPC 182": 3,
    "SPC 172": 3,
    "SPC 162": 3,
    "URC 142": 1,
    "MATH 112": 1,
    "SPC 251": 3,
    "SPC 265": 3,
    "SPC 285": 3,
    "SPC 281": 3,
    "SPC 271": 3,
    "SPC 252": 4,
    "SPC 262": 4,
    "SPC 282": 1,
    "SPC 284": 3,
    "SPC 266": 3,
    "SPC 351": 3,
    "SPC 381": 2,
    "SPC 381 LAB": 1,
    "SPC 371": 2,
    "SPC 371 LAB": 1,
    "SPC 361": 3,
    "SPC 361 LAB": 1,
    "URC 345": 1,
    "SPC 391": 1,
    "SPC 352": 2,
    "SPC 362": 2,
    "SPC 362 LAB": 1,
    "SPC 366": 2,
    "SPC 366 LAB": 1,
    "SPC 354": 2,
    "SPC 354 LAB": 1,
    "SPC 382": 2,
    "SPC 382 LAB": 1,
    "URC 346": 1,
    "SPC 461": 3,
    "SPC 481": 2,
    "SPC 483": 2,
    "SPC 491": 3,
    "SPC 471": 2,
    "SPC 473": 3,
}

total_weighted_mark = 0

while True:
    try:
        course_code = input("Enter Course Code: ")
        score = float(input("Enter your score for the course: "))
        for course in courses:
            if course_code == course:
                weighted_mark = float(score * courses[course])
                total_weighted_mark += weighted_mark
                swa = round(float(total_weighted_mark / 15), 2)


    except EOFError:
        print()
        break

print(f"Your SWA is {swa}")
sem = int(input("What semester do your results belong to? "))
total_credit_hours = sem * 15
credit_hours_last = (sem - 1) * 15
last_cwa = float(input("What was your previous semester's CWA? "))
current_cwa = round(
    float(((last_cwa * credit_hours_last) + total_weighted_mark) / total_credit_hours),
    2,
)
print(f"Your current CWA is {current_cwa}")
