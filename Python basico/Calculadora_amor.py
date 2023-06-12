# 🚨 Don't change the code below 👇
print("Bienvenid@ a la Calculadora del amor :)")
name1 = input("Cual es tu nombre?\n")
name2 = input("Cual es su nombre?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Tu puntaje es: {love_score}, Estan juntos como pastelitos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Tu puntaje es: {love_score}, Estan bien juntos.")
else:
    print(f"Tu puntaje es: {love_score}.")

