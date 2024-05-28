command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("Plane has already taken off!")
        else:
            started = True
            print("Plane has taken off.....")
    elif command == "stop":
        if not started:
            print("Plane has already landed!")
        else:
            started = False
            print("Plane has landed.")
    elif command == "help":
        print("""
start - start the plane
stop - stop the plane
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")

