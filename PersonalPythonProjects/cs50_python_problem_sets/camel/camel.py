camel_case = input("camelCase: ")
snake_case = ""
for camel in camel_case:
    if camel.isupper():
        snake_case += "_" + camel.lower()
    else:
        snake_case += camel
print(f"snake_case: {snake_case}")
