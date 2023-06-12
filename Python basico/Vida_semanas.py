# 🚨 Don't change the code below 👇
age = input("Cual es tu edad actual?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"Tu tienes {days_remaining} dias, {weeks_remaining} semanas y {months_remaining} meses")