print("Bienvenid@ a la montaña rusa :D")

height = int(input("Cual es tu altura en cm?\n"))
pago = 0

if height > 120:
    print("Puedes ingresar a la montaña rusa :)")
    age = int(input("Cual es tu edad?\n"))
    if age < 12:
        pago = 7000
        print("Por favor paga $7.000")
    elif age <= 18:
        pago = 14000
        print("Por favor paga $14.000")
    else:
        pago = 26000
        print("Por favor paga $26.000")
    
    photo = input("Quieres tomarte una foto? S o N\n")
    if photo == "S":
        pago += 2500
        print(f"Tu pago total es {pago}")
else:
    print("Lo siento, no puedes ingresar a la montaña rusa por tu estatura :(")