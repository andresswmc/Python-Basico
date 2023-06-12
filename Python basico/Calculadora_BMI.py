# 🚨 Don't change the code below 👇
height = input("Ingresa tu estatura en m: ")
weight = input("Ingresa tu peso en kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)