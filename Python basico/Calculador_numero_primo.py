#Write your code below this line 👇

def prime_checker(number):
    primo = True
    for i in range(2, number):
        if number % i == 0:
            primo = False
    if primo:
        print("Es un numero primo.")
    else:
        print("No es un numero primo.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Comprueba este numero: "))
prime_checker(number=n)