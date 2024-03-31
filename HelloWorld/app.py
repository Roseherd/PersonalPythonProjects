name = "Richard"
password = "rowus16"

Username = input("Name: ").capitalize()
Passcode = input("Password: ")

# :Username = Username.capitalize()

if Username == name and Passcode == password:
    print(f"Welcome {name}")
elif Username != name and Passcode == password:
    print("Username is wrong")
elif Username == name and Passcode != password:
    print("Password is wrong")
else:
    print("Username and Password are wrong")
