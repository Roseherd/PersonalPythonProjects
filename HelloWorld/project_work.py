print(
    """
V(a) = titre volume of  solution(ml)
P(a) = mass of sample(g) used in Glucose(a) 
Glucose(a)(%) = percentage of glucose in glucose standard
V(b) = titre volume of sample(ml)
P(b) = mass of sample(g) used in Glucose(b)
Glucose(b)(%) = percentage of glucose in sample
Sucrose(%) = percentage of sucrose in sample
"""
)


v_a = float(input("What's V(a)? "))
p_a = float(input("What's P(a)? "))

glucose_a = round(float((3.905 / 2) * ((v_a**-1.0251) / p_a) * 100), 4)

print(f"Glucose(a)(%) = {glucose_a}%")

v_b = float(input("What's V(b)? "))
p_b = float(input("What's P(b)? "))

glucose_b = round(float((3.905 / 2) * ((v_b**-1.0251) / p_b) * 100), 4)

print(f"Glucose(b)(%) = {glucose_b}%")

sucrose = round((glucose_b - glucose_a), 4)

print(f"Sucrose(%) = {sucrose}%")
