def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3900)
elif opcion == 2:
    conversor("argentinos", 104)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opcion correcta')





