# relational operator
# >
print(2 > 1)
print(1 > 2)

# >=
print(2 >= 2)
print(1 >= 2)

# <
print(1 < 2)
print(2 < 1)

# <=
print(2 <= 2)
print(2 <= 1)

# ==
print(2 == 2)
print(2 == 1)

# !=
print(2 != 1)
print(2 != 2)

# logical operator
# and
print((1 < 2) and (2 < 3))
print((1 < 2) and (3 < 2))

# or
print((1 < 2) or (3 < 2))
print((2 < 1) or (3 < 2))

# not
print(not (1 > 2))
print(not (1 < 2))

# BMI calculator
# input your height and weight
height = input("Please input your height in centimeter:\n")
weight = input("Please input your weight in kilogram:\n")

# calculate BMI
bmi = int(weight) / ((int(height) / 100) ** 2)

# BMI interpretation
if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif bmi < 24:
    print(f"Your BMI is {bmi}, and you have a normal weight.")
elif bmi < 28:
    print(f"Your BMI is {bmi}, and you are overweight.")
else:
    print(f"Your BMI is {bmi}, and you are obese.")
