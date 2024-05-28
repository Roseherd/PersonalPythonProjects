#x=month y=day z=year

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            x, y, z = date.split("/")

            x = int(x)
            y = int(y)
            if y > 31 or x > 12:
                continue
            else:
                print(f"{z}-{x:02}-{y:02}")
            break
        elif "," in date:
            date_components = date.split()
            month_number = months.index(date_components[0]) + 1
            day_number = int(date_components[1].replace(",", ""))
            year_number = int(date_components[2])
            if day_number > 31:
                continue
            else:
                print(f"{year_number}-{month_number:02}-{day_number:02}")
            break
    except ValueError:
        pass

