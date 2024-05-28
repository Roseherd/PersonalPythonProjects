#Input for the expresion
expression = input("Expression: ")

x, y, z, = expression.split(" ")

if y == "+":
    answer = int(x) + int(z)
    print(float(answer))
elif y == "-":
    answer = int(x) - int(z)
    print(float(answer))
elif y == "*":
    answer = int(x) * int(z)
    print(float(answer))
elif y == "/":
    answer = int(x) / int(z)
    print(float(answer))




