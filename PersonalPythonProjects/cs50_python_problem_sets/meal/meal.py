def main():
    time = input("What time is it? ")
    hours, minutes = time.split(":")
    0 <= int(minutes) <= 60
    0 <= int(hours) <= 23
    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")
    else:
        print("")

#Convert time from hours and minutes to minutes only
#Convert minutes only in time to hours only
#Convert
def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes)
    hours = int(hours)
    converted_minutes = int(hours) * 60
    time = int(converted_minutes) + int(minutes)
    converted_time = float(time) / 60
    return float(converted_time)

if __name__ == "__main__":
    main()







