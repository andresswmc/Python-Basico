# Funcion Simple
def greet():
    print("Hola")
    print("Como estas?")
    print("El clima no esta muy bien hoy?")
greet()

# Funciones con Inputs

def greet_name(name):
    print(f"Hola {name}")
    print(f"Como estas {name}?")
greet_name("Andres")

# Funciones con mas de 1 Input

def greet_with(nombre, ubicacion):
    print(f"Hola {nombre}")
    print(f"Estas en {ubicacion}?")

#greet_with("Jack Bauer", "Nowhere")
#greet_with("Nowhere", "Jack Bauer")
greet_with(ubicacion = "Bogota", nombre = "Andres")