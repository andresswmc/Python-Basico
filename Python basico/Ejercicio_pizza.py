# 🚨 Don't change the code below 👇
print("Bienvenid@ a Python Pizza Deliveries!")
size = input("Que tipo de tamaño quiere su pizza? P, M, or G\n")
add_pepperoni = input("Quiere adicionar pepperoni? S or N\n")
extra_cheese = input("Quiere adicionar queso extra? S or N\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "P":
    bill += 15000
elif size == "M":
    bill += 20000
elif size == "G":
    bill += 25000

if add_pepperoni == "S":
    if size == "P":
        bill += 2000
    else:
        bill += 3000

if extra_cheese == "S":
    bill += 1500

print(f"Tu pago total es de: ${bill}.")

