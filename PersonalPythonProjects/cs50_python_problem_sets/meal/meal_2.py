def main():
    time = input("What time is it? ")
    actual_time = convert(time)

    if 7.0 <= actual_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= actual_time <= 13.0:
        print("lunch time")
    elif 18.0 <= actual_time <= 19.0:
        print("dinner time")
    else:
        print("", end="")





def convert(time):

    if time.endswith("a.m."):
        replace_dict = {'a.m.': '', 'p.m.': ''}
        for old, new in replace_dict.items():
            time = time.replace(old, new)
        hours, minutes = time.split(":")
        minutes = int(minutes)
        hours = int(hours)
        #Convert time from hours and minutes to minutes only
        converted_minutes_2 = int(hours) * 60
        time = int(converted_minutes_2) + int(minutes)
        #Convert minutes only in time to hours only
        converted_time_2 = float(time) / 60
        return float(converted_time_2)
    elif time.endswith("p.m.") and time.startswith("12"):
        replace_dict = {'a.m.': '', 'p.m.': ''}
        for old, new in replace_dict.items():
            time = time.replace(old, new)
        hours, minutes = time.split(":")
        minutes = int(minutes)
        hours = int(hours)
        converted_minutes_2 = int(hours) * 60
        time = int(converted_minutes_2) + int(minutes)
        converted_time_2 = float(time) / 60
        return float(converted_time_2)
    elif time.endswith("p.m."):
        replace_dict = {'a.m.': '', 'p.m.': ''}
        for old, new in replace_dict.items():
            time = time.replace(old, new)
        hours, minutes = time.split(":")
        minutes = int(minutes)
        hours = int(hours)
        converted_minutes_2 = int(hours) * 60
        time = int(converted_minutes_2) + int(minutes)
        converted_time_2 = float(time) / 60
        time_in_24_hours = float(converted_time_2) + 12
        return time_in_24_hours
    else:
        hours, minutes = time.split(":")
        minutes = int(minutes)
        hours = int(hours)
        converted_minutes = int(hours) * 60
        time = int(converted_minutes) + int(minutes)
        converted_time = float(time) / 60
        return float(converted_time)


#Convert time from hours and minutes in am or pm to minutes only
#Create correspondence between time in am or pm and 24 hour format


if __name__ == "__main__":
    main()







