#Make an input for the greeting
kind_of_greeting = input("Greeting: ").lower().strip()

if "hello" in kind_of_greeting:
    print("$0")
elif kind_of_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
