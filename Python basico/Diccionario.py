programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again."}

#
print(programming_dictionary["Function"])

# Agregando nuevo contenido al diccionario
programming_dictionary["Loop"] = "The action of oding something over and over again."
print(programming_dictionary)

# Crear un diccionario vacio
empty_dictionary = {}

#Editar un item en el diccionario
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop en un diccionario
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])