import random

Piedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Tijeras = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [Piedra, Papel, Tijeras]

user_eleccion = int(input("Que quieres escoger? tienes tres opciones: Opc 0 Piedra, Opc 1 Papel, Opc 2 Tijeras\n"))

if user_eleccion >= 3 or user_eleccion < 0:
    print("Has escogido un numero no valido!, Has perdido :(")
else:
    print(game_images[user_eleccion])

cpu_eleccion = random.randint(0, 2)
print("El pc escogio:")
print(game_images[cpu_eleccion])


if user_eleccion == 0 and cpu_eleccion == 2:
    print("Has ganado :D")
elif cpu_eleccion == 0 and user_eleccion == 2:
    print("El pc gana :(")    
elif cpu_eleccion > user_eleccion:
    print("El pc gana :(")
elif user_eleccion > cpu_eleccion:
    print("Has ganado :D")
elif cpu_eleccion == user_eleccion:
    print("Es empate :|")