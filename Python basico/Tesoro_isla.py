print('''
                   `\-.   `
                      \ `.  `
                       \  \ |
              __.._    |   \.       S O N - G O K U
       ..---~~     ~ . |    Y
         ~-.          `|    |
            `.               `~~--.
              \                    ~.
               \                     \__. . -- -  .
         .-~~~~~      ,    ,            ~~~~~~---...._
      .-~___        ,'/  ,'/ ,'\          __...---~~~
            ~-.    /._\_( ,(/_. 7,-.    ~~---...__
           _...>-  P""6=`_/"6"~   6)    ___...--~~~
            ~~--._ \`--') `---'   9'  _..--~~~
                  ~\ ~~/_  ~~~   /`-.--~~
                    `.  ---    .'   \_
                      `. " _.-'     | ~-.,-------._
                  ..._../~~   ./       .-'    .-~~~-.
            ,--~~~ ,'...\` _./.----~~.'/    /'       `-
        _.-(      |\    `/~ _____..-' /    /      _.-~~`.
       /   |     /. ^---~~~~       ' /    /     ,'  ~.   \
      (    /    (  .           _ ' /'    /    ,/      \   )
      (`. |     `\   - - - - ~   /'      (   /         .  |
       \.\|       \            /'        \  |`.           /
       /.'\\      `\         /'           ~-\         .  /\
      /,   (        `\     /'                `.___..-      \
     | |    \         `\_/'                  //      \.     |
     | |     |                 _Seal_      /' |       |     |
''')

print("Bienvenido a la isla del tesoro :D")
print("Tu mision es encontrar el tesoro perdido :)")

choice1 = input('Estás en un cruce, ¿a dónde quieres ir?, Escribe "izquierda" o "derecha".\n').lower()

if choice1 == "izquierda":
  choice2 = input('Haz llegado a la isla, la cual esta en medio del lago. Escribe "esperar" para esperar por un bote o Escribe "nadar" para irte nadando :)\n').lower()
  if choice2 == "esperar":
    choice3 = input("Haz llegado a la isla ileso, hay una casa con tres puertas: una roja, una amarilla y una azul, cual color deseas escoger?\n").lower()
    if choice3 == "roja":
            print("Es una habitacion consumida por el fuego, Game Over :(")
    elif choice3 == "amarilla":
            print("Haz encontrado el tesoro, felicidades :D")
    elif choice3 == "azul":
            print("En la habitacion hay bestias, Game Over :(")
    else:
            print("Haz escogido una puerta que no existe, Game Over :(")
  else:
        print("Te ataco un cocodrilo, Game Over :(")
else:
    print("Game Over :(")
