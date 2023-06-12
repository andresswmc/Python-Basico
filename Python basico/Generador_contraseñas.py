# Generador de contraseñas :)

import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
caracteres = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

print("Bienvenid@ al generador de contraseñas :)")
nr_letras = int(input("Cuantas letras quieres tener en la contraseña?\n"))
nr_numeros = int(input(f"Cuantos numeros quieres tener en la contraseña?\n"))
nr_caracteres = int(input(f"Cuantos caracteres quieres tener?\n"))

# Modo Facil
#passwrd = ""

#for letra in range(1, nr_letras + 1):
#    passwrd += random.choice(letras)

#for caracter in range(1, nr_caracteres + 1):
#    passwrd += random.choice(caracteres)

#for numero in range(1, nr_numeros + 1):
#    passwrd += random.choice(numeros)

#print(passwrd)

# Modo dificil

password_lista = []

for letra in range(1, nr_letras + 1):
    password_lista.append(random.choice(letras))

for caracter in range(1, nr_caracteres + 1):
    password_lista += random.choice(caracteres)

for numero in range(1, nr_numeros + 1):
    password_lista += random.choice(numeros)

print(password_lista)
random.shuffle(password_lista)
print(password_lista)

passwd = ""
for char in password_lista:
    passwd += char

print(f"Tu nueva contraseña es: {passwd} :)")