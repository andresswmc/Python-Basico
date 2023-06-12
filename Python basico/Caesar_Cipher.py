alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alfabeto:
            posicion = alfabeto.index(char)
            nueva_posicion = posicion + shift_amount
            end_text += alfabeto[nueva_posicion]
        else:
            end_text += char
    print(f"El texto {cipher_direction}, desencriptado es: {end_text}")

from logo_Caesar import logo
print(logo)

continua = True
while continua:
    direction = input("Escribe 'encode' para encriptar o escribe 'decode' para desencriptar:\n")
    text = input("Escribe tu mensaje:\n").lower()
    shift = int(input("Escribe el numero de cambios:\n"))

    shift = shift % 26

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    resultado = input("Escribe 'Si' si quieres intentar de nuevo, de lo contrario escribe 'No'\n")
    if resultado == "No":
        continua = False
        print("Adios")

# def encripto(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         posicion = alfabeto.index(letter)
#         nueva_posicion = posicion + shift_amount
#         nueva_letra = alfabeto[nueva_posicion]
#         cipher_text += nueva_letra
#     print(f"El texto encriptado es {cipher_text}")

# def desencripto(cipher_text, shift_amount):
#     for letter in cipher_text:
#         posicion = alfabeto.index(letter)
#         nueva_posicion = posicion - shift_amount
#         plain_text += alfabeto[nueva_posicion]
#     print(f"El texto desencriptado es {plain_text}")

# if direction == "encode":
#     encripto(plain_text = text, shift_amount = shift)
# elif direction == "decode": 
#     desencripto(ciphertext = text, shift_amount = shift)

