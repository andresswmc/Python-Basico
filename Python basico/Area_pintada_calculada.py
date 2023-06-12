#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    num_cans = math.ceil(area / cover)
    print(f"Tu necesitaras {num_cans} latas de pinturas.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Altura de la pared: "))
test_w = int(input("Ancho de la pared: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)