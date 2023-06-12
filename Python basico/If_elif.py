print("Bienvenid@ a la montaña rusa :D")

height = int(input("Cual es tu altura en cm?\n"))

if height > 120:
    print("Puedes ingresar a la montaña rusa :)")
    age = int(input("Cual es tu edad?\n"))
    if age < 12:
        print("Por favor paga $7.000")
    elif age <= 18:
        print("Por favor paga $14.000")
    else:
        print("Por favor paga $26.000")
else:
    print("Lo siento, no puedes ingresar a la montaña rusa por tu estatura")