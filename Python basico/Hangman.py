import random
import os
from Hangman_lista import lista_palabras
from Hangman_stages import stages
from Hangman_arte import logo

print(logo)

fin_juego = False
lives = len(stages) - 1

busqueda_palabra = random.choice(lista_palabras)
longitud_palabra = len(busqueda_palabra)

display = []
for _ in range(len(busqueda_palabra)):
    display += "_"
print(display)

while not fin_juego:
    ingreso = input("Ingresa una letra: ").lower()
    
    os.system('cls')

    if ingreso in display:
        print(f"Ya has ingresado esta letra: {ingreso}")
    
    for position in range(len(busqueda_palabra)):
        letra = busqueda_palabra[position]
        if letra == ingreso:
            display[position] = letra
        print(f"{' '.join(display)}")

    if ingreso not in busqueda_palabra:
        print(f"La letra ingresada {ingreso}, no esta dentro de la palabra, Has perdido una vida")
    lives -= 1
    if lives == 0:
        fin_juego = True
        print("Perdiste :(")

    if "_" not in display:
        fin_juego = True
        print(" Has Ganado :)")
    
    print(stages[lives])